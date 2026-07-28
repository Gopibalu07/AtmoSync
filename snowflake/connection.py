import snowflake.connector
from .snowflake_config import *

connection = snowflake.connector.connect(
    account=ACCOUNT,
    user=USER,
    password=PASSWORD,
    warehouse=WAREHOUSE,
    database=DATABASE,
    schema=SCHEMA,
    role=ROLE
)

cursor = connection.cursor()


def insert_sensor_data(record):

    query = """
    INSERT INTO CONTAINER_SENSOR_DATA
    (
        CONTAINER_ID,
        COMMODITY,
        LOCATION,

        SOURCE_PORT,
        DESTINATION_PORT,

        LATITUDE,
        LONGITUDE,

        TEMPERATURE,
        HUMIDITY,
        VIBRATION,
        SPEED,

        BATTERY_LEVEL,

        DOOR_STATUS,
        GPS_STATUS,
        NETWORK_STATUS,

        EVENT_TYPE,

        SENSOR_STATUS,

        EVENT_TIME
    )

    VALUES
    (
        %s,%s,%s,
        %s,%s,
        %s,%s,
        %s,%s,%s,%s,
        %s,
        %s,%s,%s,
        %s,
        %s,
        %s
    )
    """

    cursor.execute(
        query,
        (
            record["container_id"],
            record["commodity"],
            record["location"],

            record["source_port"],
            record["destination_port"],

            record["latitude"],
            record["longitude"],

            record["temperature"],
            record["humidity"],
            record["vibration"],
            record["speed"],

            record["battery_level"],

            record["door_status"],
            record["gps_status"],
            record["network_status"],

            record["event_type"],

            record["sensor_status"],

            record["timestamp"]
        )
    )

    connection.commit()

    print(f"✅ Inserted -> {record['container_id']}")