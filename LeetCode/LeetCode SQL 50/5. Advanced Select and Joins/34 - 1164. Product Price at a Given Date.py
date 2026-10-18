# Databricks notebook source
# MAGIC %md
# MAGIC ## 1164. Product Price at a Given Date (Medium)
# MAGIC
# MAGIC ### Table: `Products`
# MAGIC
# MAGIC | Column Name | Type |
# MAGIC | --- | --- |
# MAGIC | `product_id` | `int` |
# MAGIC | `new_price` | `int` |
# MAGIC | `change_date` | `date` |
# MAGIC
# MAGIC * (`product_id`, `change_date`) is the primary key.
# MAGIC * Each row shows a price change for a product on a given date.
# MAGIC * Initially, all products have price `10`.
# MAGIC
# MAGIC ### Task
# MAGIC Find the prices of all products on the date `2019-08-16`.
# MAGIC
# MAGIC Return the result table in any order.
# MAGIC
# MAGIC ### Example
# MAGIC
# MAGIC **Input:** `Products`
# MAGIC
# MAGIC | product_id | new_price | change_date |
# MAGIC | --- | --- | --- |
# MAGIC | 1 | 20 | 2019-08-14 |
# MAGIC | 2 | 50 | 2019-08-14 |
# MAGIC | 1 | 30 | 2019-08-15 |
# MAGIC | 1 | 35 | 2019-08-16 |
# MAGIC | 2 | 65 | 2019-08-17 |
# MAGIC | 3 | 20 | 2019-08-18 |
# MAGIC
# MAGIC **Output:**
# MAGIC
# MAGIC | product_id | price |
# MAGIC | --- | --- |
# MAGIC | 2 | 50 |
# MAGIC | 1 | 35 |
# MAGIC | 3 | 10 |
# MAGIC
# MAGIC **Explanation:**
# MAGIC
# MAGIC * Product `1` has its latest price on `2019-08-16` updated to `35`.
# MAGIC * Product `2` has no change on `2019-08-16`, so its most recent earlier price is `50`.
# MAGIC * Product `3` has no price change on or before `2019-08-16`, so it keeps the initial price `10`.