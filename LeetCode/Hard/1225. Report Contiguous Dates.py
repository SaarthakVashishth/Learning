# Databricks notebook source
# MAGIC %md
# MAGIC ## 1225. Report Contiguous Dates
# MAGIC
# MAGIC ### Table: `Failed`
# MAGIC
# MAGIC | Column Name | Type |
# MAGIC | --- | --- |
# MAGIC | `fail_date` | `date` |
# MAGIC
# MAGIC ### Table: `Succeeded`
# MAGIC
# MAGIC | Column Name | Type |
# MAGIC | --- | --- |
# MAGIC | `success_date` | `date` |
# MAGIC
# MAGIC ### Task
# MAGIC Generate all date ranges such that:
# MAGIC
# MAGIC * each range contains continuous days
# MAGIC * all dates in the range are either all `failed` or all `succeeded`
# MAGIC
# MAGIC Return:
# MAGIC
# MAGIC | start_date | end_date | state |
# MAGIC | --- | --- | --- |
# MAGIC
# MAGIC ### Example
# MAGIC
# MAGIC **Input:** `Failed`
# MAGIC
# MAGIC | fail_date |
# MAGIC | --- |
# MAGIC | 2019-01-01 |
# MAGIC | 2019-01-02 |
# MAGIC | 2019-01-05 |
# MAGIC
# MAGIC **Input:** `Succeeded`
# MAGIC
# MAGIC | success_date |
# MAGIC | --- |
# MAGIC | 2019-01-03 |
# MAGIC | 2019-01-04 |
# MAGIC | 2019-01-06 |
# MAGIC
# MAGIC **Output:**
# MAGIC
# MAGIC | start_date | end_date | state |
# MAGIC | --- | --- | --- |
# MAGIC | 2019-01-01 | 2019-01-02 | failed |
# MAGIC | 2019-01-03 | 2019-01-04 | succeeded |
# MAGIC | 2019-01-05 | 2019-01-05 | failed |
# MAGIC | 2019-01-06 | 2019-01-06 | succeeded |
# MAGIC
# MAGIC **Explanation:**
# MAGIC
# MAGIC * `2019-01-01` to `2019-01-02` are continuous failed dates.
# MAGIC * `2019-01-03` to `2019-01-04` are continuous succeeded dates.
# MAGIC * `2019-01-05` is a failed date by itself.
# MAGIC * `2019-01-06` is a succeeded date by itself.

# COMMAND ----------

