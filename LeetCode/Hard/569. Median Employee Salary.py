# Databricks notebook source
# MAGIC %md
# MAGIC ## 569. Median Employee Salary
# MAGIC
# MAGIC ### Table: `Employee`
# MAGIC
# MAGIC | Column Name | Type |
# MAGIC | --- | --- |
# MAGIC | `id` | `int` |
# MAGIC | `company` | `varchar` |
# MAGIC | `salary` | `int` |
# MAGIC
# MAGIC * `id` contains unique values.
# MAGIC
# MAGIC ### Task
# MAGIC Find the median salary for each company.
# MAGIC
# MAGIC * If a company has an odd number of rows, return the single middle row.
# MAGIC * If a company has an even number of rows, return the two middle rows.
# MAGIC
# MAGIC Return the result table in any order.
# MAGIC
# MAGIC ### Example
# MAGIC
# MAGIC **Input:** `Employee`
# MAGIC
# MAGIC | id | company | salary |
# MAGIC | --- | --- | --- |
# MAGIC | 1 | A | 100 |
# MAGIC | 2 | A | 200 |
# MAGIC | 3 | A | 300 |
# MAGIC | 4 | B | 400 |
# MAGIC | 5 | B | 500 |
# MAGIC | 6 | B | 600 |
# MAGIC | 7 | B | 700 |
# MAGIC
# MAGIC **Output:**
# MAGIC
# MAGIC | id | company | salary |
# MAGIC | --- | --- | --- |
# MAGIC | 2 | A | 200 |
# MAGIC | 3 | A | 300 |
# MAGIC | 5 | B | 500 |
# MAGIC
# MAGIC **Explanation:**
# MAGIC
# MAGIC * Company `A` has salaries `[100, 200, 300]`, so the median row is salary `200`.
# MAGIC * Company `B` has salaries `[400, 500, 600, 700]`, so the two middle salaries are `500` and `600`.
# MAGIC
# MAGIC Following the expected output shown here, the result includes the returned median rows for each company.

# COMMAND ----------

