# Log-Analysis - Project for Fullstack Nano-Degree

## Program Overview 

This projects purpose is to build an informative summary of logs by running queries on a live database. This project was completed for Udacity's Fullstack Nanodegree and uses PostgreSQL, coding Python with DB-API, and Vagrant.

## Contents of Project

Files:
  newsdata.sql - database provided by Udacity.
  newsdata.py - SQL database - query code.

## Dependency

1. Please make sure the following are installed:
  Python3
  Vagrant (Linux-based VM)
  Virtual Box

## Running the Program

1. Download [this](https://github.com/udacity/fullstack-nanodegree-vm) and then navigate to where this repository is cloned in the terminal.
```
cd fullstack-nanodegree-vm/
cd vagrant/
```
Clone this repo in the same file as the newsdata.sql

2. Launch Vagrant with the following command:
  ```
  vagrant up
  ```
3. Log in to Vagrant using the following command:
  ```
  vagrant ssh
  ```
4. Load the data using the following command:
  ```
  psql -d news -f newsdata.sql
  ```
  This will connect to the database.

5. To run the program, use the following command:
  ```
  python3 newsdata.py
  ```

## Database contents

The database has three tables:
  1. Articles
  2. Authors
  3. Log

## Views created

View of articles title and the corresponding number of views - article_view_count
```
create view article_view_count as select b1.title, count(*) as views
from articles b1
left join log b2 on b2.path like concat('%', b1.slug)
group by b1.id, b1.title, b1.id, b2.path
order by views desc;
```

View of error count - error_count
```
create view error_count as
select date(time), count(*) as errors
from log
where status != '200 OK'
group by date(time)
order by count(status);
```

View with count of all status codes - total_status_count
```
create view total_status_count as
select date(time), count(status)      
from log
group by date(time)
order by count(status);
```

View to find percentage of error status codes in a day - find_error_percent
```
create view find_error_percent as
select error_count.date, round((100.0*error_count.errors)/total_status_count.count, 2) as percent
from error_count, total_status_count
where error_count.date = total_status_count.date;
```


## License

This program is based off of a project from [Udacity's Full Stack Web Developer Nanodegree](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004). fresh_tomatoes.py is also given by Udacity.
