# Databricks notebook source
# MAGIC %md
# MAGIC ## 602. Friend Requests II: Who Has the Most Friends (Medium)
# MAGIC
# MAGIC ### Table: `RequestAccepted`
# MAGIC
# MAGIC | Column Name | Type |
# MAGIC | --- | --- |
# MAGIC | `requester_id` | `int` |
# MAGIC | `accepter_id` | `int` |
# MAGIC | `accept_date` | `date` |
# MAGIC
# MAGIC * (`requester_id`, `accepter_id`) is the primary key.
# MAGIC * Each row records a friendship request that was accepted.
# MAGIC * Friendship is mutual once accepted.
# MAGIC
# MAGIC ### Task
# MAGIC Find the person who has the most friends and return their friend count.
# MAGIC
# MAGIC * The test cases guarantee that only one person has the most friends.
# MAGIC
# MAGIC ### Example
# MAGIC
# MAGIC **Input:** `RequestAccepted`
# MAGIC
# MAGIC | requester_id | accepter_id | accept_date |
# MAGIC | --- | --- | --- |
# MAGIC | 1 | 2 | 2016/06/03 |
# MAGIC | 1 | 3 | 2016/06/08 |
# MAGIC | 2 | 3 | 2016/06/08 |
# MAGIC | 3 | 4 | 2016/06/09 |
# MAGIC
# MAGIC **Output:**
# MAGIC
# MAGIC | id | num |
# MAGIC | --- | --- |
# MAGIC | 3 | 3 |
# MAGIC
# MAGIC **Explanation:**
# MAGIC
# MAGIC * User `3` is friends with users `1`, `2`, and `4`.
# MAGIC * That gives user `3` a total of `3` friends, which is the highest.