#!/usr/bin/env python3
import psycopg2

# Query to find the three most viewed articles, displaying title and view count:
top_articles = """select title, views from article_view_count group by title, views order
by views desc limit 3;"""

#Query to find most viewed author, displaying all authors and view count is descending order: 
most_viewed_author = """select authors.name, count(*) as views from articles join authors on
articles.author = authors.id join log on articles.slug =
substring(log.path, 10) where log.status = '200 OK' group by
authors.name order by views desc limit 3;"""

#Query to find days when error status code (404s) makes up more than 1% of the request status' of the day: 
error_percent_high ="""select date, percent from find_error_percent where percent > 1 order by
percent desc;"""

# Pass this function a query to run the above queries.
def execute_query(query):
    try:
        db = psycopg2.connect(database='news')
        cur = db.cursor()
        cur.execute(query)
        results = cur.fetchall()
        return results
    except:
        db.close();

    
# Pass in the result of queries to be properly formatted for printing
def print_results(results):
    print('------------------------------------------------')
    for row in results:
        print('%s | %d'  % row)


#Execute query and print out three most viewed articles.
def three_top_articles():
    print('\nThe three most viewed articles are:')
    print('\t\t title \t\t | views')
    top_three = execute_query(top_articles)
    print_results(top_three)


# Query and print the three most popular authors.
def three_top_authors():
    print('\n\nThe three most viewed authors are: ')
    top_authors = execute_query(most_viewed_author)
    print_results(top_authors)


def error_rate():
    print('\n\nDates that bad requests made up more than 1% of requests: ')
    error_rate = execute_query(error_percent_high)
    print('------------------------------------------------')
    for date, percent in error_rate:
        print('%s | %1.2f'  % (date, percent))
        print('\n\n')
                          
three_top_articles()
three_top_authors()
error_rate()
