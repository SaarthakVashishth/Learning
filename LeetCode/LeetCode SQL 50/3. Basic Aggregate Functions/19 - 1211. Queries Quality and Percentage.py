# Databricks notebook source
# MAGIC %md
# MAGIC ## 1211. Queries Quality and Percentage (Easy)
# MAGIC
# MAGIC ### Table: `Queries`
# MAGIC
# MAGIC | Column Name | Type |
# MAGIC | --- | --- |
# MAGIC | `query_name` | `varchar` |
# MAGIC | `result` | `varchar` |
# MAGIC | `position` | `int` |
# MAGIC | `rating` | `int` |
# MAGIC
# MAGIC * This table may contain duplicate rows.
# MAGIC * It stores information collected from database queries.
# MAGIC * `position` ranges from `1` to `500`.
# MAGIC * `rating` ranges from `1` to `5`.
# MAGIC * A query with `rating < 3` is considered a poor query.
# MAGIC
# MAGIC ### Task
# MAGIC For each `query_name`, compute:
# MAGIC
# MAGIC * `quality`, which is the average of `rating / position`
# MAGIC * `poor_query_percentage`, which is the percentage of rows with `rating < 3`
# MAGIC
# MAGIC Round both values to `2` decimal places.
# MAGIC
# MAGIC Return the result table in any order.
# MAGIC
# MAGIC ### Example
# MAGIC
# MAGIC **Input:** `Queries`
# MAGIC
# MAGIC | query_name | result | position | rating |
# MAGIC | --- | --- | --- | --- |
# MAGIC | Dog | Golden Retriever | 1 | 5 |
# MAGIC | Dog | German Shepherd | 2 | 5 |
# MAGIC | Dog | Mule | 200 | 1 |
# MAGIC | Cat | Shirazi | 5 | 2 |
# MAGIC | Cat | Siamese | 3 | 3 |
# MAGIC | Cat | Sphynx | 7 | 4 |
# MAGIC
# MAGIC **Output:**
# MAGIC
# MAGIC | query_name | quality | poor_query_percentage |
# MAGIC | --- | --- | --- |
# MAGIC | Dog | 2.50 | 33.33 |
# MAGIC | Cat | 0.66 | 33.33 |
# MAGIC
# MAGIC **Explanation:**
# MAGIC
# MAGIC * `Dog` quality is `((5 / 1) + (5 / 2) + (1 / 200)) / 3 = 2.50`.
# MAGIC * `Dog` poor query percentage is `(1 / 3) * 100 = 33.33`.
# MAGIC * `Cat` quality is `((2 / 5) + (3 / 3) + (4 / 7)) / 3 = 0.66`.
# MAGIC * `Cat` poor query percentage is `(1 / 3) * 100 = 33.33`.