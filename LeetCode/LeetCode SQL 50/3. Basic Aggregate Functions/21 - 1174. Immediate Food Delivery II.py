# Databricks notebook source
# MAGIC %md
# MAGIC ## 1174. Immediate Food Delivery II (Medium)
# MAGIC
# MAGIC ### Table: `Delivery`
# MAGIC
# MAGIC | Column Name | Type |
# MAGIC | --- | --- |
# MAGIC | `delivery_id` | `int` |
# MAGIC | `customer_id` | `int` |
# MAGIC | `order_date` | `date` |
# MAGIC | `customer_pref_delivery_date` | `date` |
# MAGIC
# MAGIC * `delivery_id` contains unique values for this table.
# MAGIC * This table stores food delivery orders and each customer's preferred delivery date.
# MAGIC * An order is `immediate` if `customer_pref_delivery_date = order_date`; otherwise it is `scheduled`.
# MAGIC * Each customer has exactly one first order, based on the earliest `order_date`.
# MAGIC
# MAGIC ### Task
# MAGIC Find the percentage of immediate orders among the first orders of all customers.
# MAGIC
# MAGIC * Only each customer's first order should be considered.
# MAGIC * Round the result to `2` decimal places.
# MAGIC
# MAGIC ### Example
# MAGIC
# MAGIC **Input:** `Delivery`
# MAGIC
# MAGIC | delivery_id | customer_id | order_date | customer_pref_delivery_date |
# MAGIC | --- | --- | --- | --- |
# MAGIC | 1 | 1 | 2019-08-01 | 2019-08-02 |
# MAGIC | 2 | 2 | 2019-08-02 | 2019-08-02 |
# MAGIC | 3 | 1 | 2019-08-11 | 2019-08-12 |
# MAGIC | 4 | 3 | 2019-08-24 | 2019-08-24 |
# MAGIC | 5 | 3 | 2019-08-21 | 2019-08-22 |
# MAGIC | 6 | 2 | 2019-08-11 | 2019-08-13 |
# MAGIC | 7 | 4 | 2019-08-09 | 2019-08-09 |
# MAGIC
# MAGIC **Output:**
# MAGIC
# MAGIC | immediate_percentage |
# MAGIC | --- |
# MAGIC | 50.00 |
# MAGIC
# MAGIC **Explanation:**
# MAGIC
# MAGIC * Customer `1` has first order `1`, which is scheduled.
# MAGIC * Customer `2` has first order `2`, which is immediate.
# MAGIC * Customer `3` has first order `5`, which is scheduled.
# MAGIC * Customer `4` has first order `7`, which is immediate.
# MAGIC * So `2` out of `4` first orders are immediate, giving `50.00`.