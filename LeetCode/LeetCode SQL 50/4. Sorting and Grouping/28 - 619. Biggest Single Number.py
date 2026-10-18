# Databricks notebook source
# MAGIC %md
# MAGIC ## 619. Biggest Single Number (Easy)
# MAGIC
# MAGIC ### Table: `MyNumbers`
# MAGIC
# MAGIC | Column Name | Type |
# MAGIC | --- | --- |
# MAGIC | `num` | `int` |
# MAGIC
# MAGIC * This table may contain duplicates.
# MAGIC * Each row stores one integer.
# MAGIC * A single number is a number that appears exactly once.
# MAGIC
# MAGIC ### Task
# MAGIC Find the largest single number.
# MAGIC
# MAGIC * If there is no single number, return `null`.
# MAGIC
# MAGIC ### Example 1
# MAGIC
# MAGIC **Input:** `MyNumbers`
# MAGIC
# MAGIC | num |
# MAGIC | --- |
# MAGIC | 8 |
# MAGIC | 8 |
# MAGIC | 3 |
# MAGIC | 3 |
# MAGIC | 1 |
# MAGIC | 4 |
# MAGIC | 5 |
# MAGIC | 6 |
# MAGIC
# MAGIC **Output:**
# MAGIC
# MAGIC | num |
# MAGIC | --- |
# MAGIC | 6 |
# MAGIC
# MAGIC **Explanation:**
# MAGIC
# MAGIC * The single numbers are `1`, `4`, `5`, and `6`.
# MAGIC * The largest of them is `6`.
# MAGIC
# MAGIC ### Example 2
# MAGIC
# MAGIC **Input:** `MyNumbers`
# MAGIC
# MAGIC | num |
# MAGIC | --- |
# MAGIC | 8 |
# MAGIC | 8 |
# MAGIC | 7 |
# MAGIC | 7 |
# MAGIC | 3 |
# MAGIC | 3 |
# MAGIC | 3 |
# MAGIC
# MAGIC **Output:**
# MAGIC
# MAGIC | num |
# MAGIC | --- |
# MAGIC | null |
# MAGIC
# MAGIC **Explanation:**
# MAGIC
# MAGIC * No number appears exactly once, so the result is `null`.