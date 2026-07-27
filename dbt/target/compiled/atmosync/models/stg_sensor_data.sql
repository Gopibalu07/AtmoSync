SELECT
    container_id,
    commodity,
    location,
    temperature,
    humidity,
    vibration,
    battery_level,
    sensor_status,
    event_time
FROM ATMOSYNC_DB.RAW_DATA.CONTAINER_SENSOR_DATA