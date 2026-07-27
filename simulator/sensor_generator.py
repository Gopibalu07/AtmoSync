import random
import time
import json
from datetime import datetime

from .config import (
    CONTAINER_IDS,
    COMMODITIES,
    LOCATIONS
)


def generate_sensor_data():

    temperature = round(random.uniform(18, 35), 2)
    humidity = round(random.uniform(50, 90), 2)
    vibration = round(random.uniform(0.1, 2.5), 2)
    battery = random.randint(50, 100)

    if temperature > 30:
        status = "CRITICAL"
    elif temperature > 27:
        status = "WARNING"
    else:
        status = "NORMAL"

    return {
        "container_id": random.choice(CONTAINER_IDS),
        "commodity": random.choice(COMMODITIES),
        "location": random.choice(LOCATIONS),
        "temperature": temperature,
        "humidity": humidity,
        "vibration": vibration,
        "battery_level": battery,
        "sensor_status": status,
        "timestamp": datetime.now().isoformat()
    }


def save_json(record):

    with open("sample_output.json", "a") as file:
        json.dump(record, file)
        file.write("\n")


def run_simulator():

    print("Starting AtmoSync IoT Simulator...\n")

    while True:

        record = generate_sensor_data()

        print(json.dumps(record, indent=4))

        save_json(record)

        print("=" * 60)

        time.sleep(3)


if __name__ == "__main__":
    run_simulator()