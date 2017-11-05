## Program Overview 

TBA

## Contents of Project

Files:
  TBD

## Dependency

Python v2+ is required to run this project. 

## Running the Program

TBD

## Views created

View of articles title and the corresponding number of views - article_view_count
```
create view article_view_count as select b1.title, count(*) as views
from articles b1
left join log b2 on b2.path like concat('%', b1.slug)
group by b1.id, b1.title, b1.id, b2.path
order by views desc;
```
Example output of article_view_count
```
               title                | views  
------------------------------------+--------
 Candidate is jerk, alleges rival   | 338647
 Bears love berries, alleges bear   | 253801
 Bad things gone, say good people   | 170098
 Goats eat Google's lawn            |  84906
 Trouble for troubled troublemakers |  84810
 Balloon goons doomed               |  84557
 There are a lot of bears           |  84504
 Media obsessed with bears          |  84383
 ```



## License

This program is based off of a project from [Udacity's Full Stack Web Developer Nanodegree](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004). fresh_tomatoes.py is also given by Udacity.
