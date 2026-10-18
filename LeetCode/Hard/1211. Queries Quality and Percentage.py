# Databricks notebook source
# MAGIC %md
# MAGIC ## 1211. Queries Quality and Percentage
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
# MAGIC ### Task
# MAGIC Define:
# MAGIC
# MAGIC * `quality` = average of (`rating / position`)
# MAGIC * `poor_query_percentage` = percentage of rows where `rating < 3`
# MAGIC
# MAGIC For each `query_name`, compute:
# MAGIC
# MAGIC * `quality`
# MAGIC * `poor_query_percentage`
# MAGIC
# MAGIC Both values should be rounded to `2` decimal places.
# MAGIC
# MAGIC ### Example
# MAGIC
# MAGIC **Input:** `Queries`
# MAGIC
# MAGIC | query_name | result | position | rating |
# MAGIC | --- | --- | --- | --- |
# MAGIC | Dog | Golden | 1 | 5 |
# MAGIC | Dog | Bulldog | 2 | 4 |
# MAGIC | Dog | Poodle | 3 | 2 |
# MAGIC | Cat | Persian | 1 | 3 |
# MAGIC | Cat | Siamese | 2 | 2 |
# MAGIC
# MAGIC **Output:**
# MAGIC
# MAGIC | query_name | quality | poor_query_percentage |
# MAGIC | --- | --- | --- |
# MAGIC | Dog | 2.67 | 33.33 |
# MAGIC | Cat | 1.75 | 50.00 |
# MAGIC
# MAGIC **Explanation:**
# MAGIC
# MAGIC For `Dog`:
# MAGIC
# MAGIC * `quality = avg(5/1, 4/2, 2/3) = 2.67`
# MAGIC * `poor_query_percentage = 1 out of 3 = 33.33`
# MAGIC
# MAGIC For `Cat`:
# MAGIC
# MAGIC * `quality = avg(3/1, 2/2) = 1.75`
# MAGIC * `poor_query_percentage = 1 out of 2 = 50.00`

# COMMAND ----------

