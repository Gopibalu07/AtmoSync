
  create or replace   view ATMOSYNC_DB.RAW_DATA.stg_commodity
  
  
  
  
  as (
    SELECT
    commodity,
    market,
    price,
    updated_time
FROM ATMOSYNC_DB.RAW_DATA.COMMODITY_PRICE
  );

