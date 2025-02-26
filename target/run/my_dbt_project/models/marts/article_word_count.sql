
  
    

    create or replace table `de-project-batch`.`newsletter`.`article_word_count`
      
    
    

    OPTIONS()
    as (
      -- models/marts/fct_article_wordcount.sql


with newsletter as (
    select
        unique_row_id,
        article,
        SPLIT(article, ' ') as words
    from `de-project-batch`.`newsletter`.`newsletter_stg`
)

select
    unique_row_id,
    ARRAY_LENGTH(words) as word_count
from newsletter
    );
  