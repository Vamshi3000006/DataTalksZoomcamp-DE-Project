
  
    

    create or replace table `de-project-batch`.`newsletter`.`facts_summary_author_per_month`
      
    
    

    OPTIONS()
    as (
      

with staged as (
    select *
    from `de-project-batch`.`newsletter`.`newsletter`
    
)

select
    DATE(date) as publication_date,
    author,section,
    count(*) as article_count,
    avg(LENGTH(article)) as avg_article_length
from staged
group by publication_date, author,section
order by  author
    );
  