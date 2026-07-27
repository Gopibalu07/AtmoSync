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
            return False, f"{field} is missing"

    return True, "Valid Record"