# Databricks notebook source
# MAGIC %md
# MAGIC ## 1251. Average Selling Price (Easy)
# MAGIC
# MAGIC ### Table: `Prices`
# MAGIC
# MAGIC | Column Name | Type |
# MAGIC | --- | --- |
# MAGIC | `product_id` | `int` |
# MAGIC | `start_date` | `date` |
# MAGIC | `end_date` | `date` |
# MAGIC | `price` | `int` |
# MAGIC
# MAGIC * (`product_id`, `start_date`, `end_date`) is the primary key.
# MAGIC * Each row stores the price of a product for a specific date range.
# MAGIC * Price periods for the same `product_id` do not overlap.
# MAGIC
# MAGIC ### Table: `UnitsSold`
# MAGIC
# MAGIC | Column Name | Type |
# MAGIC | --- | --- |
# MAGIC | `product_id` | `int` |
# MAGIC | `purchase_date` | `date` |
# MAGIC | `units` | `int` |
# MAGIC
# MAGIC * This table may contain duplicate rows.
# MAGIC * Each row stores the date and quantity sold for a product.
# MAGIC
# MAGIC ### Task
# MAGIC Find the average selling price for each product.
# MAGIC
# MAGIC * Return the result as `average_price`.
# MAGIC * Round `average_price` to `2` decimal places.
# MAGIC * If a product has no sold units, its average selling price is `0`.
# MAGIC
# MAGIC Return the result table in any order.
# MAGIC
# MAGIC ### Example
# MAGIC
# MAGIC **Input:** `Prices`
# MAGIC
# MAGIC | product_id | start_date | end_date | price |
# MAGIC | --- | --- | --- | --- |
# MAGIC | 1 | 2019-02-17 | 2019-02-28 | 5 |
# MAGIC | 1 | 2019-03-01 | 2019-03-22 | 20 |
# MAGIC | 2 | 2019-02-01 | 2019-02-20 | 15 |
# MAGIC | 2 | 2019-02-21 | 2019-03-31 | 30 |
# MAGIC
# MAGIC **Input:** `UnitsSold`
# MAGIC
# MAGIC | product_id | purchase_date | units |
# MAGIC | --- | --- | --- |
# MAGIC | 1 | 2019-02-25 | 100 |
# MAGIC | 1 | 2019-03-01 | 15 |
# MAGIC | 2 | 2019-02-10 | 200 |
# MAGIC | 2 | 2019-03-22 | 30 |
# MAGIC
# MAGIC **Output:**
# MAGIC
# MAGIC | product_id | average_price |
# MAGIC | --- | --- |
# MAGIC | 1 | 6.96 |
# MAGIC | 2 | 16.96 |
# MAGIC
# MAGIC **Explanation:**
# MAGIC
# MAGIC * Average selling price is total revenue divided by total units sold.
# MAGIC * Product `1`: `((100 * 5) + (15 * 20)) / 115 = 6.96`.
# MAGIC * Product `2`: `((200 * 15) + (30 * 30)) / 230 = 16.96`.