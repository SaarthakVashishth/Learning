# Databricks notebook source
# MAGIC %md
# MAGIC ## 601. Human Traffic of Stadium
# MAGIC
# MAGIC ### Table: `Stadium`
# MAGIC
# MAGIC | Column Name | Type |
# MAGIC | --- | --- |
# MAGIC | `id` | `int` |
# MAGIC | `visit_date` | `date` |
# MAGIC | `people` | `int` |
# MAGIC
# MAGIC * `id` is the primary key.
# MAGIC * `id` increases sequentially.
# MAGIC
# MAGIC ### Task
# MAGIC Display records that belong to groups of `3` or more consecutive rows where:
# MAGIC
# MAGIC * the number of people is greater than or equal to `100`
# MAGIC
# MAGIC Return the result table ordered by `visit_date`.
# MAGIC
# MAGIC ### Example
# MAGIC
# MAGIC **Input:** `Stadium`
# MAGIC
# MAGIC | id | visit_date | people |
# MAGIC | --- | --- | --- |
# MAGIC | 1 | 2017-01-01 | 10 |
# MAGIC | 2 | 2017-01-02 | 109 |
# MAGIC | 3 | 2017-01-03 | 150 |
# MAGIC | 4 | 2017-01-04 | 99 |
# MAGIC | 5 | 2017-01-05 | 145 |
# MAGIC | 6 | 2017-01-06 | 145 |
# MAGIC | 7 | 2017-01-07 | 145 |
# MAGIC
# MAGIC **Output:**
# MAGIC
# MAGIC | id | visit_date | people |
# MAGIC | --- | --- | --- |
# MAGIC | 5 | 2017-01-05 | 145 |
# MAGIC | 6 | 2017-01-06 | 145 |
# MAGIC | 7 | 2017-01-07 | 145 |
# MAGIC
# MAGIC **Explanation:**
# MAGIC
# MAGIC * Rows `(2, 3)` have only `2` consecutive rows with `people >= 100`, so they are excluded.
# MAGIC * Rows `(5, 6, 7)` form `3` consecutive rows with `people >= 100`, so they are included.

# COMMAND ----------

