# Databricks notebook source
# MAGIC %md
# MAGIC ## 1907. Count Salary Categories (Medium)
# MAGIC
# MAGIC ### Table: `Accounts`
# MAGIC
# MAGIC | Column Name | Type |
# MAGIC | --- | --- |
# MAGIC | `account_id` | `int` |
# MAGIC | `income` | `int` |
# MAGIC
# MAGIC * `account_id` is the primary key.
# MAGIC * Each row stores the monthly income for one bank account.
# MAGIC
# MAGIC ### Task
# MAGIC Calculate the number of bank accounts in each salary category.
# MAGIC
# MAGIC Salary categories are:
# MAGIC * `Low Salary`: income strictly less than `20000`
# MAGIC * `Average Salary`: income from `20000` to `50000` inclusive
# MAGIC * `High Salary`: income strictly greater than `50000`
# MAGIC
# MAGIC The result must contain all three categories. If a category has no accounts, return `0`.
# MAGIC
# MAGIC Return the result table in any order.
# MAGIC
# MAGIC ### Example
# MAGIC
# MAGIC **Input:** `Accounts`
# MAGIC
# MAGIC | account_id | income |
# MAGIC | --- | --- |
# MAGIC | 3 | 108939 |
# MAGIC | 2 | 12747 |
# MAGIC | 8 | 87709 |
# MAGIC | 6 | 91796 |
# MAGIC
# MAGIC **Output:**
# MAGIC
# MAGIC | category | accounts_count |
# MAGIC | --- | --- |
# MAGIC | Low Salary | 1 |
# MAGIC | Average Salary | 0 |
# MAGIC | High Salary | 3 |
# MAGIC
# MAGIC **Explanation:**
# MAGIC
# MAGIC * `Low Salary`: account `2`
# MAGIC * `Average Salary`: no accounts
# MAGIC * `High Salary`: accounts `3`, `6`, and `8`