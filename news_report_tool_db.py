#!/usr/bin/env python3Example

import psycopg2
import bleach

DBNAME = "news"


"""
    This file is responsible for execute queries which will result
    the answers for Nanodegree Developer Web Full-Stack Program.

    Credits: Udacity lessons and Python Documentation
    https://docs.python.org/3/
"""


# Returns how many views and
# the name of the viewed article.
def get_three_most_popular_articles():
    connection = get_db_connection()
    cursor = connection.cursor()

    query = "  select count(l.id), a.title "
    query += " from log as l "
    query += " join articles as a on l.path like '%' || a.slug "
    query += " where status = '200 OK' "
    query += " and path like '/article/%' "
    query += " group by a.title "
    query += " order by count(l.id) desc "
    query += " limit 3 "

    cursor.execute(query)
    popular_articles = cursor.fetchall()
    connection.close()

    return popular_articles


# Returns how many views and
# the name of the author that
# publish the viewed articles.
def get_most_popular_authors():
    connection = get_db_connection()
    cursor = connection.cursor()

    query = " select count(l.id), au.name "
    query += " from log as l "
    query += " join articles as a on l.path like '%' || a.slug "
    query += " join authors as au on au.id = a.author "
    query += " where l.status = '200 OK' "
    query += " and l.path like '/article/%' "
    query += " group by au.name "
    query += " order by count(l.id) desc "

    cursor.execute(query)
    popular_authors = cursor.fetchall()
    connection.close()

    return popular_authors


# Returns the day and the percentage of the errors
# happened in that day.
def get_days_more_than_one_percent_errors():
    connection = get_db_connection()
    cursor = connection.cursor()

    query = " select to_char(l.time, 'Month DD, YYYY'), "
    query += " le.log_errors * 100 / count(l.id) as percentual "
    query += "        from ( "
    query += "          select count(l2.id) as log_errors, "
    query += "          to_char(l2.time, 'Month DD, YYYY') as date "
    query += "          from log as l2 "
    query += "          where l2.status != '200 OK' "
    query += "          group by to_char(l2.time, 'Month DD, YYYY') "
    query += "        ) as le,  "
    query += " log as l "
    query += " where le.date = to_char(l.time, 'Month DD, YYYY')   "
    query += " group by le.log_errors, to_char(l.time, 'Month DD, YYYY') "
    query += " having le.log_errors * 100 / count(l.id) > 1 "
    query += " order by percentual desc, to_char(l.time, 'Month DD, YYYY')  "

    cursor.execute(query)

    days_more_than_one_percent_errors = cursor.fetchall()
    connection.close

    return days_more_than_one_percent_errors


# Return a db connection.
def get_db_connection():
    return psycopg2.connect(database=DBNAME)
