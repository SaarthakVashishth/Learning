# Databricks notebook source
# MAGIC %md
# MAGIC ## 1141. User Activity for the Past 30 Days I (Easy)
# MAGIC
# MAGIC ### Table: `Activity`
# MAGIC
# MAGIC | Column Name | Type |
# MAGIC | --- | --- |
# MAGIC | `user_id` | `int` |
# MAGIC | `session_id` | `int` |
# MAGIC | `activity_date` | `date` |
# MAGIC | `activity_type` | `enum` |
# MAGIC
# MAGIC * This table may contain duplicate rows.
# MAGIC * `activity_type` can be `open_session`, `end_session`, `scroll_down`, or `send_message`.
# MAGIC * This table records user activity for a social media website.
# MAGIC * Each session belongs to exactly one user.
# MAGIC
# MAGIC ### Task
# MAGIC Find the daily active user count for the `30`-day period ending on `2019-07-27` inclusive.
# MAGIC
# MAGIC * A user is active on a day if they performed at least one activity on that day.
# MAGIC * Days with zero active users do not need to appear in the result.
# MAGIC
# MAGIC Return the result table in any order.
# MAGIC
# MAGIC ### Example
# MAGIC
# MAGIC **Input:** `Activity`
# MAGIC
# MAGIC | user_id | session_id | activity_date | activity_type |
# MAGIC | --- | --- | --- | --- |
# MAGIC | 1 | 1 | 2019-07-20 | open_session |
# MAGIC | 1 | 1 | 2019-07-20 | scroll_down |
# MAGIC | 1 | 1 | 2019-07-20 | end_session |
# MAGIC | 2 | 4 | 2019-07-20 | open_session |
# MAGIC | 2 | 4 | 2019-07-21 | send_message |
# MAGIC | 2 | 4 | 2019-07-21 | end_session |
# MAGIC | 3 | 2 | 2019-07-21 | open_session |
# MAGIC | 3 | 2 | 2019-07-21 | send_message |
# MAGIC | 3 | 2 | 2019-07-21 | end_session |
# MAGIC | 4 | 3 | 2019-06-25 | open_session |
# MAGIC | 4 | 3 | 2019-06-25 | end_session |
# MAGIC
# MAGIC **Output:**
# MAGIC
# MAGIC | day | active_users |
# MAGIC | --- | --- |
# MAGIC | 2019-07-20 | 2 |
# MAGIC | 2019-07-21 | 2 |
# MAGIC
# MAGIC **Explanation:**
# MAGIC
# MAGIC * On `2019-07-20`, users `1` and `2` were active.
# MAGIC * On `2019-07-21`, users `2` and `3` were active.
# MAGIC * Days with zero active users are not included.