
  
    

    create or replace table `de-project-batch`.`newsletter`.`newsletter_stg`
      
    
    

    OPTIONS()
    as (
      

with raw as (
    select *
    from `de-project-batch`.`newsletter`.`newsletter`
),

clean as (
    select
      unique_row_id,
      cast(date as timestamp) as date,
      cast(year as int64) as year,
      cast(month as int64) as month,
      cast(day as int64) as day,
      author,
      title,
      article,
      url,
      section,
      publication
    from raw
)

select * from clean
    );
  