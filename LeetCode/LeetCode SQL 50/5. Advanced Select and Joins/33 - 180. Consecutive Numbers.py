# Databricks notebook source
# MAGIC %md
# MAGIC ## 180. Consecutive Numbers (Medium)
# MAGIC
# MAGIC ### Table: `Logs`
# MAGIC
# MAGIC | Column Name | Type |
# MAGIC | --- | --- |
# MAGIC | `id` | `int` |
# MAGIC | `num` | `varchar` |
# MAGIC
# MAGIC * `id` is the primary key.
# MAGIC * `id` is an auto-increment column starting from `1`.
# MAGIC
# MAGIC ### Task
# MAGIC Find all numbers that appear at least `3` times consecutively.
# MAGIC
# MAGIC Return the result table in any order.
# MAGIC
# MAGIC ### Example
# MAGIC
# MAGIC **Input:** `Logs`
# MAGIC
# MAGIC | id | num |
# MAGIC | --- | --- |
# MAGIC | 1 | 1 |
# MAGIC | 2 | 1 |
# MAGIC | 3 | 1 |
# MAGIC | 4 | 2 |
# MAGIC | 5 | 1 |
# MAGIC | 6 | 2 |
# MAGIC | 7 | 2 |
# MAGIC
# MAGIC **Output:**
# MAGIC
# MAGIC | ConsecutiveNums |
# MAGIC | --- |
# MAGIC | 1 |
# MAGIC
# MAGIC **Explanation:**
# MAGIC
# MAGIC * The number `1` appears in three consecutive rows with IDs `1`, `2`, and `3`.
# MAGIC * No other number appears at least three times in a row.