
  create or replace   view ATMOSYNC_DB.RAW_DATA.stg_commodity
  
  
  
  
  as (
    SELECT
    COMMODITY,
    PRICE_PER_KG,
    CURRENCY,
    LAST_UPDATED
FROM ATMOSYNC_DB.RAW_DATA.COMMODITY_PRICE
  );

