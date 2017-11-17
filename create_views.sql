create view article_view_count as select b1.title, count(*) as views
from articles b1
left join log b2 on b2.path = '/article/' || b1.slug
group by b1.id, b1.title, b1.id, b2.path
order by views desc;

create view error_count as
select date(time), count(*) as errors
from log
where status != '200 OK'
group by date(time)
order by count(status);

create view total_status_count as
select date(time), count(status)      
from log
group by date(time)
order by count(status);

create view find_error_percent as
select error_count.date, round((100.0*error_count.errors)/total_status_count.count, 2) as percent
from error_count, total_status_count
where error_count.date = total_status_count.date;
