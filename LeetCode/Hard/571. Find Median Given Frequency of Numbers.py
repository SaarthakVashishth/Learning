# Databricks notebook source
# MAGIC %md
# MAGIC ## 571. Find Median Given Frequency of Numbers
# MAGIC
# MAGIC ### Table: `Numbers`
# MAGIC
# MAGIC | Column Name | Type |
# MAGIC | --- | --- |
# MAGIC | `Number` | `int` |
# MAGIC | `Frequency` | `int` |
# MAGIC
# MAGIC * `Number` is the value.
# MAGIC * `Frequency` is the number of times that value occurs.
# MAGIC * The `Numbers` table stores values with their frequency.
# MAGIC
# MAGIC ### Task
# MAGIC Find the median of all the numbers, considering their frequencies.
# MAGIC
# MAGIC Return the result rounded to `1` decimal place.
# MAGIC
# MAGIC ### Example
# MAGIC
# MAGIC **Input:** `Numbers`
# MAGIC
# MAGIC | Number | Frequency |
# MAGIC | --- | --- |
# MAGIC | 0 | 7 |
# MAGIC | 1 | 1 |
# MAGIC | 2 | 3 |
# MAGIC | 3 | 1 |
# MAGIC
# MAGIC **Output:**
# MAGIC
# MAGIC | median |
# MAGIC | --- |
# MAGIC | 0.0 |
# MAGIC
# MAGIC **Explanation:**
# MAGIC
# MAGIC The expanded array is:
# MAGIC
# MAGIC `[0,0,0,0,0,0,0,1,2,2,2,3]`
# MAGIC
# MAGIC The median is the average of the middle element(s), which gives `0.0`.

# COMMAND ----------

