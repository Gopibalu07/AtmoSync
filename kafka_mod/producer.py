import json
from kafka import KafkaProducer

from .kafka_config import BOOTSTRAP_SERVERS, TOPIC_NAME

producer = KafkaProducer(
    bootstrap_servers=BOOTSTRAP_SERVERS,
    value_serializer=lambda value: json.dumps(value).encode("utf-8")
)

def send_sensor_data(sensor_data):
    producer.send(TOPIC_NAME, sensor_data)
    producer.flush()

    print(f"Sent -> {sensor_data['container_id']} | {sensor_data['timestamp']}")