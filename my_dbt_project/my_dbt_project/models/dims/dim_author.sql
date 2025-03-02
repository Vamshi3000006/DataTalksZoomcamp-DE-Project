-- models/dims/dim_author.sql


with authors as (
    select distinct author
    from `de-project-batch`.`newsletter`.`newsletter_stg`
)

select
    author,
    count(*) over () as total_authors
from authors