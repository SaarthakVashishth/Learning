# Databricks notebook source
# MAGIC %md
# MAGIC ## 1045. Customers Who Bought All Products (Medium)
# MAGIC
# MAGIC ### Table: `Customer`
# MAGIC
# MAGIC | Column Name | Type |
# MAGIC | --- | --- |
# MAGIC | `customer_id` | `int` |
# MAGIC | `product_key` | `int` |
# MAGIC
# MAGIC * This table may contain duplicate rows.
# MAGIC * `customer_id` is not null.
# MAGIC * `product_key` is a foreign key referencing `Product`.
# MAGIC * Each row shows that a customer bought a product.
# MAGIC
# MAGIC ### Table: `Product`
# MAGIC
# MAGIC | Column Name | Type |
# MAGIC | --- | --- |
# MAGIC | `product_key` | `int` |
# MAGIC
# MAGIC * `product_key` is the primary key.
# MAGIC * Each row stores one product.
# MAGIC
# MAGIC ### Task
# MAGIC Report the customer IDs of customers who bought all products in the `Product` table.
# MAGIC
# MAGIC Return the result table in any order.
# MAGIC
# MAGIC ### Example
# MAGIC
# MAGIC **Input:** `Customer`
# MAGIC
# MAGIC | customer_id | product_key |
# MAGIC | --- | --- |
# MAGIC | 1 | 5 |
# MAGIC | 2 | 6 |
# MAGIC | 3 | 5 |
# MAGIC | 3 | 6 |
# MAGIC | 1 | 6 |
# MAGIC
# MAGIC **Input:** `Product`
# MAGIC
# MAGIC | product_key |
# MAGIC | --- |
# MAGIC | 5 |
# MAGIC | 6 |
# MAGIC
# MAGIC **Output:**
# MAGIC
# MAGIC | customer_id |
# MAGIC | --- |
# MAGIC | 1 |
# MAGIC | 3 |
# MAGIC
# MAGIC **Explanation:**
# MAGIC
# MAGIC * Customers `1` and `3` bought both products `5` and `6`.
# MAGIC * Customer `2` bought only product `6`, so they are excluded.