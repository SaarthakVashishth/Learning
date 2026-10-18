# Databricks notebook source
# MAGIC %md
# MAGIC ## 1158. Market Analysis II
# MAGIC
# MAGIC ### Table: `Users`
# MAGIC
# MAGIC | Column Name | Type |
# MAGIC | --- | --- |
# MAGIC | `user_id` | `int` |
# MAGIC | `join_date` | `date` |
# MAGIC | `favorite_brand` | `varchar` |
# MAGIC
# MAGIC ### Table: `Orders`
# MAGIC
# MAGIC | Column Name | Type |
# MAGIC | --- | --- |
# MAGIC | `order_id` | `int` |
# MAGIC | `order_date` | `date` |
# MAGIC | `item_id` | `int` |
# MAGIC | `buyer_id` | `int` |
# MAGIC | `seller_id` | `int` |
# MAGIC
# MAGIC ### Table: `Items`
# MAGIC
# MAGIC | Column Name | Type |
# MAGIC | --- | --- |
# MAGIC | `item_id` | `int` |
# MAGIC | `item_brand` | `varchar` |
# MAGIC
# MAGIC ### Task
# MAGIC For each seller, determine whether the brand of the second item they sold is equal to their favorite brand.
# MAGIC
# MAGIC Return:
# MAGIC
# MAGIC * `seller_id`
# MAGIC * `2nd_item_fav_brand` with values `yes` or `no`
# MAGIC
# MAGIC If a seller sold fewer than `2` items, return `no`.
# MAGIC
# MAGIC ### Example
# MAGIC
# MAGIC **Input:** `Users`
# MAGIC
# MAGIC | user_id | join_date | favorite_brand |
# MAGIC | --- | --- | --- |
# MAGIC | 1 | 2018-01-01 | Lenovo |
# MAGIC | 2 | 2018-02-09 | Samsung |
# MAGIC | 3 | 2018-01-19 | LG |
# MAGIC
# MAGIC **Input:** `Orders`
# MAGIC
# MAGIC | order_id | order_date | item_id | buyer_id | seller_id |
# MAGIC | --- | --- | --- | --- | --- |
# MAGIC | 1 | 2019-08-01 | 4 | 1 | 2 |
# MAGIC | 2 | 2019-08-02 | 2 | 1 | 3 |
# MAGIC | 3 | 2019-08-03 | 3 | 2 | 3 |
# MAGIC | 4 | 2019-08-04 | 1 | 4 | 2 |
# MAGIC
# MAGIC **Input:** `Items`
# MAGIC
# MAGIC | item_id | item_brand |
# MAGIC | --- | --- |
# MAGIC | 1 | Samsung |
# MAGIC | 2 | Lenovo |
# MAGIC | 3 | LG |
# MAGIC | 4 | HP |
# MAGIC
# MAGIC **Output:**
# MAGIC
# MAGIC | seller_id | 2nd_item_fav_brand |
# MAGIC | --- | --- |
# MAGIC | 2 | yes |
# MAGIC | 3 | no |
# MAGIC
# MAGIC **Explanation:**
# MAGIC
# MAGIC * Seller `2` sold item `4` first and item `1` second. The second item brand is `Samsung`, which matches their favorite brand, so the result is `yes`.
# MAGIC * Seller `3` sold item `2` first and item `3` second. The second item brand does not match their favorite brand, so the result is `no`.

# COMMAND ----------

