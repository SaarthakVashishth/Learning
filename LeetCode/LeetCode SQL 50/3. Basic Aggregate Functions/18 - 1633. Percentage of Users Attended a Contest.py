# Databricks notebook source
# MAGIC %md
# MAGIC ## 1633. Percentage of Users Attended a Contest (Easy)
# MAGIC
# MAGIC ### Table: `Users`
# MAGIC
# MAGIC | Column Name | Type |
# MAGIC | --- | --- |
# MAGIC | `user_id` | `int` |
# MAGIC | `user_name` | `varchar` |
# MAGIC
# MAGIC * `user_id` is the primary key.
# MAGIC * Each row stores a user's ID and name.
# MAGIC
# MAGIC ### Table: `Register`
# MAGIC
# MAGIC | Column Name | Type |
# MAGIC | --- | --- |
# MAGIC | `contest_id` | `int` |
# MAGIC | `user_id` | `int` |
# MAGIC
# MAGIC * (`contest_id`, `user_id`) is the primary key.
# MAGIC * Each row shows a user registered in a contest.
# MAGIC
# MAGIC ### Task
# MAGIC Find the percentage of users registered in each contest.
# MAGIC
# MAGIC * Round the percentage to `2` decimal places.
# MAGIC * Order the result by `percentage` in descending order.
# MAGIC * If there is a tie, order by `contest_id` in ascending order.
# MAGIC
# MAGIC ### Example
# MAGIC
# MAGIC **Input:** `Users`
# MAGIC
# MAGIC | user_id | user_name |
# MAGIC | --- | --- |
# MAGIC | 6 | Alice |
# MAGIC | 2 | Bob |
# MAGIC | 7 | Alex |
# MAGIC
# MAGIC **Input:** `Register`
# MAGIC
# MAGIC | contest_id | user_id |
# MAGIC | --- | --- |
# MAGIC | 215 | 6 |
# MAGIC | 209 | 2 |
# MAGIC | 208 | 2 |
# MAGIC | 210 | 6 |
# MAGIC | 208 | 6 |
# MAGIC | 209 | 7 |
# MAGIC | 209 | 6 |
# MAGIC | 215 | 7 |
# MAGIC | 208 | 7 |
# MAGIC | 210 | 2 |
# MAGIC | 207 | 2 |
# MAGIC | 210 | 7 |
# MAGIC
# MAGIC **Output:**
# MAGIC
# MAGIC | contest_id | percentage |
# MAGIC | --- | --- |
# MAGIC | 208 | 100.0 |
# MAGIC | 209 | 100.0 |
# MAGIC | 210 | 100.0 |
# MAGIC | 215 | 66.67 |
# MAGIC | 207 | 33.33 |
# MAGIC
# MAGIC **Explanation:**
# MAGIC
# MAGIC * All users registered in contests `208`, `209`, and `210`, so each has `100.0`.
# MAGIC * Contests are sorted by percentage descending, then by `contest_id` ascending for ties.
# MAGIC * Contest `215` has `2` of `3` users, which is `66.67`.
# MAGIC * Contest `207` has `1` of `3` users, which is `33.33`.