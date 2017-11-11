#!/usr/bin/env python3
import psycopg2


# Query to find the three most viewed articles, displaying title and view count:
top_articles = """select title, views from article_view_count group by title, views order by views desc limit 3;"""

#Query to find most viewed author, displaying all authors and view count is descending order: 
most_viewed_author = """select a.name, count(*) as views from authors a left join articles b1 on a.id = b1.id left join log b2 on b2.path like concat('%', b1.slug) group by a.name order by views desc;"""

#Query to find days when error status code (404s) makes up more than 1% of the request status' of the day: 
error_percent_high ="""select date, percent from find_error_percent where percent > 1 order by find_error_percent desc;"""

# Call this to run the above queries.
def execute_query(query):
    db = psycopg2.connect(database="news")
    cur = db.cursor()
    cur.execute(query)
    results = cur.fetchall()
    db.close();
    return results

#Execute query and print out three most viewed articles.
def three_top_articles():
    top_three = execute_query(top_articles)

    #print out the results in a readable format
    print('\nThe three most viewed articles are:')
    print('\n\n\t\t title \t\t | views')
    print('---------------------------------+--------')

    for title, views in top_three:
        print("%s | %d" % (title,views))


# Query and print the three most popular authors.
def three_top_authors():
    top_authors = execute_query(most_viewed_author)
    print('\n\nThe three most viewed authors are: ')
    print('-----------------------------------------')

    for name, views in top_authors:
        print("%s - %d" % (name,views))


def error_rate():
    error_rate = execute_query(error_percent_high)
    print('\n\nDates that bad requests made up more than 1% of requests: ')
    print('-------------------------')

    for date, percent in error_rate:
        print("       %s | %d" % (date,percent))
              
                          
three_top_articles()
three_top_authors()
error_rate()
