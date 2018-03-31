#!/usr/bin/env python3

import news_report_tool_db as news_db
from models import Article


"""

    This file is responsible to get all
    the answers of the question for the
    Log analysis project from Udacity -
    Nanodegree Developer Web Full-Stack
    Program.

    Credits: Udacity lessons and Python Documentation
    https://docs.python.org/3/

    Questions:
        1 - What are the most popular
            three articles of all time?

        2 - Who are the most popular
            article authors of all time?

        3 - On which days did more than
            percent of requests lead
            to errors?
"""


def print_answer_first_question():
    articles_views = news_db.get_three_most_popular_articles()

    print("\nWhat are the most popular articles of all time?\n")
    for article_view in articles_views:
        print(article_view[1] + " - " + str(article_view[0]) + " Views")


def print_answer_second_question():
    most_popular_authors = news_db.get_most_popular_authors()

    print("\nWho are the most popular authors of all time?\n")
    for popular_author in most_popular_authors:
        print(popular_author[1] + " - " + str(popular_author[0]) + " Views")


def print_answer_third_question():
    days_with_errors = news_db.get_days_more_than_one_percent_errors()

    print("\nOn which days did more than percent of "
          "requests lead to errors?\n")
    for day_with_errors in days_with_errors:
        print(day_with_errors[0] + " - " + str(day_with_errors[1]) + "%")

print_answer_first_question()
print_answer_second_question()
print_answer_third_question()
