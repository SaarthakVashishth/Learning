# Databricks notebook source
# MAGIC %md
# MAGIC ## 1193. Monthly Transactions I (Medium)
# MAGIC
# MAGIC ### Table: `Transactions`
# MAGIC
# MAGIC | Column Name | Type |
# MAGIC | --- | --- |
# MAGIC | `id` | `int` |
# MAGIC | `country` | `varchar` |
# MAGIC | `state` | `enum` |
# MAGIC | `amount` | `int` |
# MAGIC | `trans_date` | `date` |
# MAGIC
# MAGIC * `id` is the primary key.
# MAGIC * This table stores incoming transactions.
# MAGIC * `state` is an enum with values `approved` and `declined`.
# MAGIC
# MAGIC ### Task
# MAGIC For each month and country, report:
# MAGIC
# MAGIC * the total number of transactions as `trans_count`
# MAGIC * the number of approved transactions as `approved_count`
# MAGIC * the total transaction amount as `trans_total_amount`
# MAGIC * the approved transaction amount as `approved_total_amount`
# MAGIC
# MAGIC Return the result table in any order.
# MAGIC
# MAGIC ### Example
# MAGIC
# MAGIC **Input:** `Transactions`
# MAGIC
# MAGIC | id | country | state | amount | trans_date |
# MAGIC | --- | --- | --- | --- | --- |
# MAGIC | 121 | US | approved | 1000 | 2018-12-18 |
# MAGIC | 122 | US | declined | 2000 | 2018-12-19 |
# MAGIC | 123 | US | approved | 2000 | 2019-01-01 |
# MAGIC | 124 | DE | approved | 2000 | 2019-01-07 |
# MAGIC
# MAGIC **Output:**
# MAGIC
# MAGIC | month | country | trans_count | approved_count | trans_total_amount | approved_total_amount |
# MAGIC | --- | --- | --- | --- | --- | --- |
# MAGIC | 2018-12 | US | 2 | 1 | 3000 | 1000 |
# MAGIC | 2019-01 | US | 1 | 1 | 2000 | 2000 |
# MAGIC | 2019-01 | DE | 1 | 1 | 2000 | 2000 |
# MAGIC
# MAGIC **Explanation:**
# MAGIC
# MAGIC * In `2018-12`, the `US` has `2` transactions totaling `3000`, with `1` approved transaction totaling `1000`.
# MAGIC * In `2019-01`, the `US` has `1` approved transaction totaling `2000`.
# MAGIC * In `2019-01`, `DE` also has `1` approved transaction totaling `2000`.