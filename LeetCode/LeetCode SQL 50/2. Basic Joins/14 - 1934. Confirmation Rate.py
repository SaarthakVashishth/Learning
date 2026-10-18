# Databricks notebook source
# DBTITLE 1,Cell 1
# MAGIC %md
# MAGIC ## 1934. Confirmation Rate (Medium)
# MAGIC
# MAGIC ### Table: `Signups`
# MAGIC
# MAGIC | Column Name | Type |
# MAGIC | --- | --- |
# MAGIC | `user_id` | `int` |
# MAGIC | `time_stamp` | `datetime` |
# MAGIC
# MAGIC * `user_id` contains unique values for this table.
# MAGIC * Each row records the signup time for a user.
# MAGIC
# MAGIC ### Table: `Confirmations`
# MAGIC
# MAGIC | Column Name | Type |
# MAGIC | --- | --- |
# MAGIC | `user_id` | `int` |
# MAGIC | `time_stamp` | `datetime` |
# MAGIC | `action` | `ENUM` |
# MAGIC
# MAGIC * (`user_id`, `time_stamp`) is the primary key.
# MAGIC * `user_id` is a foreign key referencing `Signups`.
# MAGIC * `action` can be either `confirmed` or `timeout`.
# MAGIC * Each row records whether a confirmation request was confirmed or timed out.
# MAGIC
# MAGIC ### Task
# MAGIC For each user, compute the confirmation rate:
# MAGIC
# MAGIC * `confirmed messages / total confirmation requests`
# MAGIC * If a user made no confirmation requests, their confirmation rate is `0`.
# MAGIC * Round the result to `2` decimal places.
# MAGIC
# MAGIC Return the result table in any order.
# MAGIC
# MAGIC ### Example
# MAGIC
# MAGIC **Input:** `Signups`
# MAGIC
# MAGIC | user_id | time_stamp |
# MAGIC | --- | --- |
# MAGIC | 3 | 2020-03-21 10:16:13 |
# MAGIC | 7 | 2020-01-04 13:57:59 |
# MAGIC | 2 | 2020-07-29 23:09:44 |
# MAGIC | 6 | 2020-12-09 10:39:37 |
# MAGIC
# MAGIC **Input:** `Confirmations`
# MAGIC
# MAGIC | user_id | time_stamp | action |
# MAGIC | --- | --- | --- |
# MAGIC | 3 | 2021-01-06 03:30:46 | timeout |
# MAGIC | 3 | 2021-07-14 14:00:00 | timeout |
# MAGIC | 7 | 2021-06-12 11:57:29 | confirmed |
# MAGIC | 7 | 2021-06-13 12:58:28 | confirmed |
# MAGIC | 7 | 2021-06-14 13:59:27 | confirmed |
# MAGIC | 2 | 2021-01-22 00:00:00 | confirmed |
# MAGIC | 2 | 2021-02-28 23:59:59 | timeout |
# MAGIC
# MAGIC **Output:**
# MAGIC
# MAGIC | user_id | confirmation_rate |
# MAGIC | --- | --- |
# MAGIC | 6 | 0.00 |
# MAGIC | 3 | 0.00 |
# MAGIC | 7 | 1.00 |
# MAGIC | 2 | 0.50 |
# MAGIC
# MAGIC **Explanation:**
# MAGIC
# MAGIC * User `6` made no confirmation requests, so the rate is `0.00`.
# MAGIC * User `3` made `2` requests and both timed out, so the rate is `0.00`.
# MAGIC * User `7` made `3` requests and all were confirmed, so the rate is `1.00`.
# MAGIC * User `2` made `2` requests, with `1` confirmed, so the rate is `0.50`.