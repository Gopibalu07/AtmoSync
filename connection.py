
import snowflake.connector
from snowflake_config import *


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
        TEMPERATURE,
        HUMIDITY,
        VIBRATION,
        BATTERY_LEVEL,
        SENSOR_STATUS,
        EVENT_TIME
    )
    VALUES
    (
        %s,%s,%s,%s,%s,%s,%s,%s,%s
    )
    """

    cursor.execute(
        query,
        (
            record["container_id"],
            record["commodity"],
            record["location"],
            record["temperature"],
            record["humidity"],
            record["vibration"],
            record["battery_level"],
            record["sensor_status"],
            record["timestamp"]
        )
    )

    connection.commit()

    print(f"Inserted -> {record['container_id']}")