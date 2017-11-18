create view article_view_count as 
SELECT b1.title, views
from articles b1
left join (
  SELECT path, count(*) AS views
  FROM log
  GROUP BY path
) b2 
on b2.path = '/article/' || b1.slug
order by views desc;

create view error_count as
SELECT date(time), count(*) as errors
FROM log
WHERE status != '200 OK'
GROUP BY date(time)
ORDER BY count(status);

create view total_status_count as
SELECT date(time), count(status)      
FROM log
GROUP BY date(time)
ORDER BY count(status);

create view find_error_percent as
SELECT error_count.date, round((100.0*error_count.errors)/total_status_count.count, 2) as percent
FROM error_count, total_status_count
WHERE error_count.date = total_status_count.date;
 
