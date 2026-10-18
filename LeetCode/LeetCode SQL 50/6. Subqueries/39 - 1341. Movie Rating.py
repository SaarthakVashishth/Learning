# Databricks notebook source
# MAGIC %md
# MAGIC ## 1341. Movie Rating (Medium)
# MAGIC
# MAGIC ### Table: `Movies`
# MAGIC
# MAGIC | Column Name | Type |
# MAGIC | --- | --- |
# MAGIC | `movie_id` | `int` |
# MAGIC | `title` | `varchar` |
# MAGIC
# MAGIC * `movie_id` is the primary key.
# MAGIC * `title` is unique.
# MAGIC
# MAGIC ### Table: `Users`
# MAGIC
# MAGIC | Column Name | Type |
# MAGIC | --- | --- |
# MAGIC | `user_id` | `int` |
# MAGIC | `name` | `varchar` |
# MAGIC
# MAGIC * `user_id` is the primary key.
# MAGIC * `name` is unique.
# MAGIC
# MAGIC ### Table: `MovieRating`
# MAGIC
# MAGIC | Column Name | Type |
# MAGIC | --- | --- |
# MAGIC | `movie_id` | `int` |
# MAGIC | `user_id` | `int` |
# MAGIC | `rating` | `int` |
# MAGIC | `created_at` | `date` |
# MAGIC
# MAGIC * (`movie_id`, `user_id`) is the primary key.
# MAGIC * Each row stores a user's rating for a movie.
# MAGIC * `created_at` is the review date.
# MAGIC
# MAGIC ### Task
# MAGIC Return two results:
# MAGIC
# MAGIC * the name of the user who rated the greatest number of movies
# MAGIC * the movie name with the highest average rating in February 2020
# MAGIC
# MAGIC Tie-breaking rules:
# MAGIC * for users, return the lexicographically smaller name
# MAGIC * for movies, return the lexicographically smaller title
# MAGIC
# MAGIC ### Example
# MAGIC
# MAGIC **Input:** `Movies`
# MAGIC
# MAGIC | movie_id | title |
# MAGIC | --- | --- |
# MAGIC | 1 | Avengers |
# MAGIC | 2 | Frozen 2 |
# MAGIC | 3 | Joker |
# MAGIC
# MAGIC **Input:** `Users`
# MAGIC
# MAGIC | user_id | name |
# MAGIC | --- | --- |
# MAGIC | 1 | Daniel |
# MAGIC | 2 | Monica |
# MAGIC | 3 | Maria |
# MAGIC | 4 | James |
# MAGIC
# MAGIC **Input:** `MovieRating`
# MAGIC
# MAGIC | movie_id | user_id | rating | created_at |
# MAGIC | --- | --- | --- | --- |
# MAGIC | 1 | 1 | 3 | 2020-01-12 |
# MAGIC | 1 | 2 | 4 | 2020-02-11 |
# MAGIC | 1 | 3 | 2 | 2020-02-12 |
# MAGIC | 1 | 4 | 1 | 2020-01-01 |
# MAGIC | 2 | 1 | 5 | 2020-02-17 |
# MAGIC | 2 | 2 | 2 | 2020-02-01 |
# MAGIC | 2 | 3 | 2 | 2020-03-01 |
# MAGIC | 3 | 1 | 3 | 2020-02-22 |
# MAGIC | 3 | 2 | 4 | 2020-02-25 |
# MAGIC
# MAGIC **Output:**
# MAGIC
# MAGIC | results |
# MAGIC | --- |
# MAGIC | Daniel |
# MAGIC | Frozen 2 |
# MAGIC
# MAGIC **Explanation:**
# MAGIC
# MAGIC * `Daniel` and `Monica` each rated `3` movies, so the lexicographically smaller name `Daniel` is returned.
# MAGIC * In February 2020, `Frozen 2` and `Joker` both have an average rating of `3.5`, so the lexicographically smaller title `Frozen 2` is returned.