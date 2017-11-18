#!/usr/bin/env python3
import psycopg2

# Query to find the three most viewed articles, displaying title and view count
top_articles = """SELECT title, views
                  FROM article_view_count
                  ORDER BY views DESC
                  LIMIT 3;"""

# Query to find top 3 most viewed authors.
most_viewed_author = """SELECT authors.name, count(*) as views
                        FROM articles join authors
                        ON articles.author = authors.id
                        JOIN log
                        ON '/article/' || articles.slug = log.path
                        WHERE log.status = '200 OK'
                        GROUP BY authors.name
                        ORDER BY views desc limit 3;"""

# Query to find days when error status code (404s) makes up more than 1%
# of the request status' of the day:
error_percent_high = """SELECT date, percent
                        FROM find_error_percent
                        WHERE percent > 1
                        ORDER BY percent desc;"""


# Pass this function a query to run the above queries.
def execute_query(query):
    """execute_query takes an SQL query as a parameter. It then
       executes the query, returning the results as a list of tuples.
       Args:
            query - an SQL query statement to be executed.
       Returns:
            List of tuples containing the results of the query.
    """
    try:
        db = psycopg2.connect(database='news')
        cur = db.cursor()
        cur.execute(query)
        results = cur.fetchall()
        db.close()
        return results
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)


# Pass in the result of queries to be properly formatted for printing
def print_results(results):
    """print_results takes in a result of an SQL query. It then formats it
       for printing.
       Args:
            result - result returned from SQL query.
       Output:
            Prints out the result nicely formatted.
    """
    print('-'*50)
    for row in results:
        print('{0:<35}|{1:>10}'.format(row[0], row[1]))


# Execute query and print out three most viewed articles.
def three_top_articles():
    print('\nThe three most viewed articles are:\n')
    print('\t\t title \t\t   | views')
    top_three = execute_query(top_articles)
    print_results(top_three)


# Query and print the three most popular authors.
def three_top_authors():
    print('\n\nThe three most viewed authors are:\n')
    print('\t\t author \t   | views')
    top_authors = execute_query(most_viewed_author)
    print_results(top_authors)


def error_rate():
    print('\n\nDates that bad requests made up more than 1% of requests: ')
    error_rate = execute_query(error_percent_high)
    print('-'*60)
    for date, percent in error_rate:
        print("{0:%B %d, %Y} - {1:.2f}% errors".format(date, percent))
        print('\n\n')


if __name__ == '__main__':
    three_top_articles()
    three_top_authors()
    error_rate()
