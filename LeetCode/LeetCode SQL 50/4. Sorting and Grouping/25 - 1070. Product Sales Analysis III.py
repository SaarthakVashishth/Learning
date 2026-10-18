# Databricks notebook source
# MAGIC %md
# MAGIC ## 1070. Product Sales Analysis III (Medium)
# MAGIC
# MAGIC ### Table: `Sales`
# MAGIC
# MAGIC | Column Name | Type |
# MAGIC | --- | --- |
# MAGIC | `sale_id` | `int` |
# MAGIC | `product_id` | `int` |
# MAGIC | `year` | `int` |
# MAGIC | `quantity` | `int` |
# MAGIC | `price` | `int` |
# MAGIC
# MAGIC * (`sale_id`, `year`) is the primary key.
# MAGIC * Each row records a sale of a product in a given year.
# MAGIC * A product may have multiple sales entries in the same year.
# MAGIC * `price` is the per-unit price.
# MAGIC
# MAGIC ### Task
# MAGIC Find all sales that occurred in the first year each product was sold.
# MAGIC
# MAGIC For each `product_id`:
# MAGIC * identify the earliest year it appears in `Sales`
# MAGIC * return all sales entries for that product in that year
# MAGIC
# MAGIC Return the columns `product_id`, `first_year`, `quantity`, and `price` in any order.
# MAGIC
# MAGIC ### Example
# MAGIC
# MAGIC **Input:** `Sales`
# MAGIC
# MAGIC | sale_id | product_id | year | quantity | price |
# MAGIC | --- | --- | --- | --- | --- |
# MAGIC | 1 | 100 | 2008 | 10 | 5000 |
# MAGIC | 2 | 100 | 2009 | 12 | 5000 |
# MAGIC | 7 | 200 | 2011 | 15 | 9000 |
# MAGIC
# MAGIC **Output:**
# MAGIC
# MAGIC | product_id | first_year | quantity | price |
# MAGIC | --- | --- | --- | --- |
# MAGIC | 100 | 2008 | 10 | 5000 |
# MAGIC | 200 | 2011 | 15 | 9000 |
# MAGIC
# MAGIC **Explanation:**
# MAGIC
# MAGIC * Product `100` first appears in `2008`, so that year's sale is returned.
# MAGIC * Product `200` first appears in `2011`, so that row is returned.