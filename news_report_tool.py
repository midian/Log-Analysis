#!/usr/bin/env python3

import news_report_tool_db as news_db

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
    """
    Print the answer of the first question
    """
    articles_views = news_db.get_three_most_popular_articles()

    print("\nWhat are the most popular articles of all time?\n")
    for views, title in articles_views:
        print("{} - {} Views".format(title, views))


def print_answer_second_question():
    """
    Print the answer of the second question
    """
    most_popular_authors = news_db.get_most_popular_authors()

    print("\nWho are the most popular authors of all time?\n")
    for views, author in most_popular_authors:
        print("{} - {} Views".format(author, views))


def print_answer_third_question():
    """
    Print the answer of the third question
    """
    days_with_errors = news_db.get_days_more_than_one_percent_errors()

    print("\nOn which days did more than percent of "
          "requests lead to errors?\n")
    for date, error in days_with_errors:
        print("{} - {}%".format(date, error))


def main():
    """Generate the report log."""
    print_answer_first_question()
    print_answer_second_question()
    print_answer_third_question()


if __name__ == '__main__':
    main()
