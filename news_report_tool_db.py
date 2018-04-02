#!/usr/bin/env python3

import psycopg2

DBNAME = "news"


"""
    This file is responsible for execute queries which will result
    the answers for Nanodegree Developer Web Full-Stack Program.

    Credits: Udacity lessons and Python Documentation
    https://docs.python.org/3/
"""


def get_three_most_popular_articles():
    """
    Returns how many views and
    the name of the viewed article.
    """
    query = """
            SELECT COUNT(l.id), a.title
            FROM log AS l
            JOIN articles AS a ON l.path = '/article/' || a.slug
            WHERE status = '200 OK'
            AND l.path LIKE '/article/%'
            GROUP BY a.title
            ORDER BY COUNT(l.id) DESC
            limit 3
            """

    return execute_query_statement(query)


def get_most_popular_authors():
    """
    Returns how many views and
    the name of the author that
    publish the viewed articles.
    """
    query = """
            SELECT COUNT(l.id), au.name
            FROM log AS l
            JOIN articles AS a ON l.path LIKE '%' || a.slug
            JOIN authors AS au ON au.id = a.author
            WHERE l.status = '200 OK'
            AND l.path LIKE '/article/%'
            GROUP BY au.name
            ORDER BY COUNT(l.id) DESC
            """

    return execute_query_statement(query)


def get_days_more_than_one_percent_errors():
    """
    Returns the day and the percentage of the errors
    happened in that day.
    """
    query = """
            SELECT TO_CHAR(l.time, 'Month DD, YYYY'),
            ROUND(CAST(le.log_errors *
                       CAST(100 AS FLOAT) / COUNT(l.id)
                  AS NUMERIC), 2) AS percentual
                   FROM (
                     SELECT count(l2.id) AS log_errors,
                     TO_CHAR(l2.time, 'Month DD, YYYY') AS DATE
                     FROM log AS l2
                     WHERE l2.status != '200 OK'
                     GROUP BY TO_CHAR(l2.time, 'Month DD, YYYY')
                   ) AS le,
            log AS l
            WHERE le.date = TO_CHAR(l.time, 'Month DD, YYYY')
            GROUP BY le.log_errors, TO_CHAR(l.time, 'Month DD, YYYY')
            HAVING le.log_errors * 100 / COUNT(l.id) > 1
            ORDER BY percentual DESC, TO_CHAR(l.time, 'Month DD, YYYY')
            """

    return execute_query_statement(query)


def execute_query_statement(query):
    """
    Execute and return the result of the
    query statement.
    """
    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute(query)

    result = cursor.fetchall()
    connection.close

    return result


def get_db_connection():
    """
    Return a db connection.
    """
    try:
        return psycopg2.connect(database=DBNAME)
    except Exception:
        print("Error to connect to the database.")
