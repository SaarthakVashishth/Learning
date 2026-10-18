# Databricks notebook source
# MAGIC %md
# MAGIC ## 626. Exchange Seats (Medium)
# MAGIC
# MAGIC ### Table: `Seat`
# MAGIC
# MAGIC | Column Name | Type |
# MAGIC | --- | --- |
# MAGIC | `id` | `int` |
# MAGIC | `student` | `varchar` |
# MAGIC
# MAGIC * `id` is the primary key.
# MAGIC * The ID sequence starts from `1` and increases continuously.
# MAGIC * Each row stores a student's seat ID and name.
# MAGIC
# MAGIC ### Task
# MAGIC Swap the seat ID of every two consecutive students.
# MAGIC
# MAGIC * If the number of students is odd, the last student's seat is not swapped.
# MAGIC * Return the result table ordered by `id` in ascending order.
# MAGIC
# MAGIC ### Example
# MAGIC
# MAGIC **Input:** `Seat`
# MAGIC
# MAGIC | id | student |
# MAGIC | --- | --- |
# MAGIC | 1 | Abbot |
# MAGIC | 2 | Doris |
# MAGIC | 3 | Emerson |
# MAGIC | 4 | Green |
# MAGIC | 5 | Jeames |
# MAGIC
# MAGIC **Output:**
# MAGIC
# MAGIC | id | student |
# MAGIC | --- | --- |
# MAGIC | 1 | Doris |
# MAGIC | 2 | Abbot |
# MAGIC | 3 | Green |
# MAGIC | 4 | Emerson |
# MAGIC | 5 | Jeames |
# MAGIC
# MAGIC **Explanation:**
# MAGIC
# MAGIC * Students in seats `1` and `2` are swapped.
# MAGIC * Students in seats `3` and `4` are swapped.
# MAGIC * Since there is an odd number of students, seat `5` remains unchanged.