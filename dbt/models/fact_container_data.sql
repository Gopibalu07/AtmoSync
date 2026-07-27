SELECT

s.container_id,

s.commodity,

s.location,

s.temperature,

s.humidity,

s.vibration,

s.battery_level,

s.sensor_status,

c.market,

c.price,

s.event_time

FROM {{ ref('stg_sensor_data') }} s

JOIN {{ ref('stg_commodity') }} c

ON s.commodity = c.commodity