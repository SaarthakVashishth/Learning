# Databricks notebook source
# MAGIC %md
# MAGIC ## 1729. Find Followers Count (Easy)
# MAGIC
# MAGIC ### Table: `Followers`
# MAGIC
# MAGIC | Column Name | Type |
# MAGIC | --- | --- |
# MAGIC | `user_id` | `int` |
# MAGIC | `follower_id` | `int` |
# MAGIC
# MAGIC * (`user_id`, `follower_id`) is the primary key.
# MAGIC * Each row shows that `follower_id` follows `user_id` in a social media app.
# MAGIC
# MAGIC ### Task
# MAGIC For each user, return the number of followers.
# MAGIC
# MAGIC Return the result table ordered by `user_id` in ascending order.
# MAGIC
# MAGIC ### Example
# MAGIC
# MAGIC **Input:** `Followers`
# MAGIC
# MAGIC | user_id | follower_id |
# MAGIC | --- | --- |
# MAGIC | 0 | 1 |
# MAGIC | 1 | 0 |
# MAGIC | 2 | 0 |
# MAGIC | 2 | 1 |
# MAGIC
# MAGIC **Output:**
# MAGIC
# MAGIC | user_id | followers_count |
# MAGIC | --- | --- |
# MAGIC | 0 | 1 |
# MAGIC | 1 | 1 |
# MAGIC | 2 | 2 |
# MAGIC
# MAGIC **Explanation:**
# MAGIC
# MAGIC * User `0` is followed by `{1}`.
# MAGIC * User `1` is followed by `{0}`.
# MAGIC * User `2` is followed by `{0, 1}`.