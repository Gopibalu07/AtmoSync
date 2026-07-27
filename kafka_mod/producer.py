import json
from kafka import KafkaProducer
from kafka.errors import KafkaError

from kafka_mod.kafka_config import (
    BOOTSTRAP_SERVERS,
    TOPIC_NAME
)


producer = KafkaProducer(
    bootstrap_servers=BOOTSTRAP_SERVERS,
    value_serializer=lambda value: json.dumps(value).encode("utf-8"),
    retries=5,
    acks="all"
)


REQUIRED_FIELDS = [
    "container_id",
    "commodity",
    "location",
    "temperature",
    "humidity",
    "vibration",
    "battery_level",
    "sensor_status",
    "timestamp"
]


def validate_record(record):

    for field in REQUIRED_FIELDS:

        if field not in record:
            return False, f"Missing Field : {field}"

    return True, "Valid"


def send_sensor_data(sensor_data):

    valid, message = validate_record(sensor_data)

    if not valid:
        print(f"[ERROR] {message}")
        return

    try:

        future = producer.send(TOPIC_NAME, sensor_data)

        metadata = future.get(timeout=10)

        producer.flush()

        print("=" * 60)
        print("[SUCCESS] Message Sent")
        print(f"Topic      : {metadata.topic}")
        print(f"Partition  : {metadata.partition}")
        print(f"Offset     : {metadata.offset}")
        print(f"Container  : {sensor_data['container_id']}")
        print("=" * 60)

    except KafkaError as e:

        print("=" * 60)
        print("[KAFKA ERROR]")
        print(e)
        print("=" * 60)

    except Exception as e:

        print("=" * 60)
        print("[UNKNOWN ERROR]")
        print(e)
        print("=" * 60)