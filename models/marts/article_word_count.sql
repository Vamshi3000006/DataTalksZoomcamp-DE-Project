-- models/marts/fct_article_wordcount.sql
{{
    config(
        materialized='table'
    )
}}
-- hint: This model is a fact table that contains the word count of each article
with newsletter as (
    select
        unique_row_id,
        article,
        SPLIT(article, ' ') as words
    from {{ ref('newsletter_stg') }}
)

select
    unique_row_id,
    ARRAY_LENGTH(words) as word_count
from newsletter
