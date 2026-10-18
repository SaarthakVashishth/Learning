# Databricks notebook source
# MAGIC %md
# MAGIC ## 1321. Restaurant Growth (Medium)
# MAGIC
# MAGIC ### Table: `Customer`
# MAGIC
# MAGIC | Column Name | Type |
# MAGIC | --- | --- |
# MAGIC | `customer_id` | `int` |
# MAGIC | `name` | `varchar` |
# MAGIC | `visited_on` | `date` |
# MAGIC | `amount` | `int` |
# MAGIC
# MAGIC * (`customer_id`, `visited_on`) is the primary key.
# MAGIC * This table stores restaurant customer transactions.
# MAGIC * There is at least one customer every day.
# MAGIC
# MAGIC ### Task
# MAGIC Compute the moving average of customer spending over a `7`-day window.
# MAGIC
# MAGIC * Each window includes the current day and the previous `6` days.
# MAGIC * Return `amount` as the total spending in the 7-day window.
# MAGIC * Return `average_amount` as the average spending over the 7-day window, rounded to `2` decimal places.
# MAGIC * Order the result by `visited_on` in ascending order.
# MAGIC
# MAGIC ### Example
# MAGIC
# MAGIC **Input:** `Customer`
# MAGIC
# MAGIC | customer_id | name | visited_on | amount |
# MAGIC | --- | --- | --- | --- |
# MAGIC | 1 | Jhon | 2019-01-01 | 100 |
# MAGIC | 2 | Daniel | 2019-01-02 | 110 |
# MAGIC | 3 | Jade | 2019-01-03 | 120 |
# MAGIC | 4 | Khaled | 2019-01-04 | 130 |
# MAGIC | 5 | Winston | 2019-01-05 | 110 |
# MAGIC | 6 | Elvis | 2019-01-06 | 140 |
# MAGIC | 7 | Anna | 2019-01-07 | 150 |
# MAGIC | 8 | Maria | 2019-01-08 | 80 |
# MAGIC | 9 | Jaze | 2019-01-09 | 110 |
# MAGIC | 1 | Jhon | 2019-01-10 | 130 |
# MAGIC | 3 | Jade | 2019-01-10 | 150 |
# MAGIC
# MAGIC **Output:**
# MAGIC
# MAGIC | visited_on | amount | average_amount |
# MAGIC | --- | --- | --- |
# MAGIC | 2019-01-07 | 860 | 122.86 |
# MAGIC | 2019-01-08 | 840 | 120 |
# MAGIC | 2019-01-09 | 840 | 120 |
# MAGIC | 2019-01-10 | 1000 | 142.86 |
# MAGIC
# MAGIC **Explanation:**
# MAGIC
# MAGIC * From `2019-01-01` to `2019-01-07`, the total is `860`, so the average is `122.86`.
# MAGIC * From `2019-01-02` to `2019-01-08`, the total is `840`, so the average is `120`.
# MAGIC * From `2019-01-03` to `2019-01-09`, the total is `840`, so the average is `120`.
# MAGIC * From `2019-01-04` to `2019-01-10`, the total is `1000`, so the average is `142.86`.