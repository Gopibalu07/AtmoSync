import json
from kafka import KafkaConsumer

from .kafka_config import BOOTSTRAP_SERVERS, TOPIC_NAME
from snowflake.connection import insert_sensor_data

consumer = KafkaConsumer(
    TOPIC_NAME,
    bootstrap_servers=BOOTSTRAP_SERVERS,
    auto_offset_reset="earliest",
    value_deserializer=lambda x: json.loads(x.decode("utf-8"))
)

print("\nListening for Sensor Data...\n")

for message in consumer:

    record = message.value

    print("=" * 60)
    print(json.dumps(record, indent=4))
    print("=" * 60)

    insert_sensor_data(record)