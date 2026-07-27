SELECT
    commodity,
    market,
    price,
    updated_time
FROM {{ source('raw', 'COMMODITY_PRICE') }}