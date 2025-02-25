-- models/dims/dim_author.sql
{{
    config(
        materialized='table'
    )
}}

with authors as (
    select distinct author
    from {{ ref('newsletter_stg') }}
)

select
    author,
    count(*) over () as total_authors
from authors
