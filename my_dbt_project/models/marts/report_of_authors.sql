

with summary as (
    select *
    from `de-project-batch`.`newsletter`.`facts_summary_author_per_month`
),
authors as (
    select *
    from `de-project-batch`.`newsletter`.`dim_author`
)

select
    s.publication_date,
    s.author,
    a.total_authors,
    s.section,
    s.article_count,
    s.avg_article_length
from summary s
left join authors a
  on s.author = a.author
order by s.publication_date, s.author