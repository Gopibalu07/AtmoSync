import json

from kafka import KafkaConsumer
from kafka.errors import KafkaError

from kafka_mod.kafka_config import (
    BOOTSTRAP_SERVERS,
    TOPIC_NAME
)

consumer = KafkaConsumer(
    TOPIC_NAME,
    bootstrap_servers=BOOTSTRAP_SERVERS,
    auto_offset_reset="earliest",
    enable_auto_commit=True,
    value_deserializer=lambda x: json.loads(x.decode("utf-8"))
)

print("\nKafka Consumer Started...\n")

while True:

    try:

        for message in consumer:

            try:

                record = message.value

                print("=" * 70)
                print("[MESSAGE RECEIVED]")
                print(f"Topic        : {message.topic}")
                print(f"Partition    : {message.partition}")
                print(f"Offset       : {message.offset}")
                print(f"Container ID : {record.get('container_id')}")
                print(f"Commodity    : {record.get('commodity')}")
                print(f"Location     : {record.get('location')}")
                print(f"Temperature  : {record.get('temperature')} °C")
                print(f"Humidity     : {record.get('humidity')} %")
                print(f"Vibration    : {record.get('vibration')}")
                print(f"Battery      : {record.get('battery_level')} %")
                print(f"Status       : {record.get('sensor_status')}")
                print(f"Timestamp    : {record.get('timestamp')}")
                print("- JSON Payload -")
                print(json.dumps(record, indent=4))
                print("=" * 70)

            except KeyError as e:

                print(f"[KEY ERROR] Missing Field : {e}")

            except json.JSONDecodeError:

                print("[JSON ERROR] Invalid JSON Format")

            except Exception as e:

                print(f"[MESSAGE ERROR] {e}")

    except KafkaError as e:

        print(f"[KAFKA ERROR] {e}")

    except KeyboardInterrupt:

        print("\nConsumer Stopped Successfully")
        break

    except Exception as e:

        print(f"[UNKNOWN ERROR] {e}")