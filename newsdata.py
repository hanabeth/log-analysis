# Database code from the DB newsdata.

import psycopg2

DATABASE = "newsdata"

def get_mos_viewed():
    """Return the article title and number of views in descending order"""
    db = psycopg2.connect(dbname=DATABASE)
    cur = db.cursor()
    cur.execute("select articles.title, sum(log.path) as views from articles join log where articles.slug = log.path order by desc")
    return cur.fetchall()
    db.close();
