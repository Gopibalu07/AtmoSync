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
FROM {{ source('raw', 'CONTAINER_SENSOR_DATA') }}