# Databricks notebook source
# MAGIC %md
# MAGIC ## 2356. Number of Unique Subjects Taught by Each Teacher (Easy)
# MAGIC
# MAGIC ### Table: `Teacher`
# MAGIC
# MAGIC | Column Name | Type |
# MAGIC | --- | --- |
# MAGIC | `teacher_id` | `int` |
# MAGIC | `subject_id` | `int` |
# MAGIC | `dept_id` | `int` |
# MAGIC
# MAGIC * (`subject_id`, `dept_id`) is the primary key.
# MAGIC * Each row indicates that a teacher teaches a subject in a department.
# MAGIC
# MAGIC ### Task
# MAGIC Calculate the number of unique subjects taught by each teacher.
# MAGIC
# MAGIC Return the result table in any order.
# MAGIC
# MAGIC ### Example
# MAGIC
# MAGIC **Input:** `Teacher`
# MAGIC
# MAGIC | teacher_id | subject_id | dept_id |
# MAGIC | --- | --- | --- |
# MAGIC | 1 | 2 | 3 |
# MAGIC | 1 | 2 | 4 |
# MAGIC | 1 | 3 | 3 |
# MAGIC | 2 | 1 | 1 |
# MAGIC | 2 | 2 | 1 |
# MAGIC | 2 | 3 | 1 |
# MAGIC | 2 | 4 | 1 |
# MAGIC
# MAGIC **Output:**
# MAGIC
# MAGIC | teacher_id | cnt |
# MAGIC | --- | --- |
# MAGIC | 1 | 2 |
# MAGIC | 2 | 4 |
# MAGIC
# MAGIC **Explanation:**
# MAGIC
# MAGIC * Teacher `1` teaches subject `2` in two departments and subject `3` in one department, so the unique subject count is `2`.
# MAGIC * Teacher `2` teaches subjects `1`, `2`, `3`, and `4`, so the count is `4`.