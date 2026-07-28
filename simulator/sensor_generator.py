import json
import random
import time
from datetime import datetime

from kafka_mod.producer import send_sensor_data

from .config import (
    CONTAINERS,
    INTERVAL,
    ABNORMAL_PROBABILITY
)

battery_level = 100


def generate_temperature(base_temp):

    temp = base_temp + random.uniform(-0.5, 0.5)

    if random.random() < ABNORMAL_PROBABILITY:
        temp += random.uniform(8, 12)

    return round(temp, 2)


def generate_humidity(base_humidity):

    humidity = base_humidity + random.uniform(-2, 2)

    if random.random() < ABNORMAL_PROBABILITY:
        humidity += random.uniform(15, 20)

    return round(min(humidity, 100), 2)


def generate_vibration():

    vibration = random.uniform(0.2, 2.0)

    if random.random() < ABNORMAL_PROBABILITY:
        vibration = random.uniform(3.5, 5.0)

    return round(vibration, 2)


def generate_speed():

    return round(random.uniform(18, 35), 2)


def generate_battery():

    global battery_level

    battery_level -= random.randint(0, 2)

    if battery_level <= 15:
        battery_level = 100

    return battery_level


def generate_door_status():

    if random.random() < 0.02:
        return "OPEN"

    return "CLOSED"


def generate_gps_status():

    return random.choice([
        "ACTIVE",
        "ACTIVE",
        "ACTIVE",
        "LOST"
    ])


def generate_network():

    return random.choice([
        "GOOD",
        "GOOD",
        "MEDIUM",
        "LOW"
    ])


def generate_event(temp, humidity, vibration):

    if temp >= 35:
        return "HIGH_TEMPERATURE"

    elif humidity >= 90:
        return "HIGH_HUMIDITY"

    elif vibration >= 4:
        return "HIGH_VIBRATION"

    return "NORMAL"


def generate_sensor_status(temp, humidity, vibration):

    if temp >= 35 or humidity >= 85 or vibration >= 4:
        return "CRITICAL"

    elif temp >= 30 or humidity >= 75 or vibration >= 2:
        return "WARNING"

    return "NORMAL"


def generate_sensor_record(container):

    temperature = generate_temperature(
        container["base_temperature"]
    )

    humidity = generate_humidity(
        container["base_humidity"]
    )

    vibration = generate_vibration()

    return {

        "container_id": container["container_id"],
        "commodity": container["commodity"],

        "location": container["location"],

        "source_port": container["source_port"],
        "destination_port": container["destination_port"],

        "latitude": container["latitude"],
        "longitude": container["longitude"],

        "temperature": temperature,
        "humidity": humidity,
        "vibration": vibration,

        "speed": generate_speed(),

        "battery_level": generate_battery(),

        "door_status": generate_door_status(),

        "gps_status": generate_gps_status(),

        "network_status": generate_network(),

        "event_type": generate_event(
            temperature,
            humidity,
            vibration
        ),

        "sensor_status": generate_sensor_status(
            temperature,
            humidity,
            vibration
        ),

        "timestamp": datetime.now().isoformat()

    }


def print_record(record):

    print("=" * 70)

    print(f"Container ID      : {record['container_id']}")
    print(f"Commodity         : {record['commodity']}")
    print(f"Location          : {record['location']}")
    print(f"Source Port       : {record['source_port']}")
    print(f"Destination Port  : {record['destination_port']}")
    print(f"Latitude          : {record['latitude']}")
    print(f"Longitude         : {record['longitude']}")
    print(f"Temperature       : {record['temperature']} °C")
    print(f"Humidity          : {record['humidity']} %")
    print(f"Vibration         : {record['vibration']}")
    print(f"Speed             : {record['speed']} km/h")
    print(f"Battery           : {record['battery_level']} %")
    print(f"Door Status       : {record['door_status']}")
    print(f"GPS Status        : {record['gps_status']}")
    print(f"Network           : {record['network_status']}")
    print(f"Event             : {record['event_type']}")
    print(f"Sensor Status     : {record['sensor_status']}")
    print(f"Timestamp         : {record['timestamp']}")

    print("\nJSON Payload")

    print(json.dumps(record, indent=4))

    print("=" * 70)


def run_simulator():

    print("\nStarting AtmoSync Week-2 Simulator...\n")

    while True:

        for container in CONTAINERS:

            record = generate_sensor_record(container)

            print_record(record)

            send_sensor_data(record)

            time.sleep(INTERVAL)


if __name__ == "__main__":
    run_simulator()