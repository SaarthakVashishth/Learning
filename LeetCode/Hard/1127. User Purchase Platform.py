# Databricks notebook source
# MAGIC %md
# MAGIC ## 1127. User Purchase Platform
# MAGIC
# MAGIC ### Table: `Spending`
# MAGIC
# MAGIC | Column Name | Type |
# MAGIC | --- | --- |
# MAGIC | `user_id` | `int` |
# MAGIC | `spend_date` | `date` |
# MAGIC | `platform` | `enum` |
# MAGIC | `amount` | `int` |
# MAGIC
# MAGIC * `platform` is an enum with values `('desktop', 'mobile')`.
# MAGIC * The `Spending` table records purchases made by users on different platforms for each date.
# MAGIC
# MAGIC ### Task
# MAGIC For each `spend_date`, calculate the number of users and the total amount spent for each of these categories:
# MAGIC
# MAGIC * `desktop`: users who only made purchases on desktop on that date
# MAGIC * `mobile`: users who only made purchases on mobile on that date
# MAGIC * `both`: users who made purchases on both platforms on that date
# MAGIC
# MAGIC Return the result table in any order.
# MAGIC
# MAGIC ### Example
# MAGIC
# MAGIC **Input:** `Spending`
# MAGIC
# MAGIC | user_id | spend_date | platform | amount |
# MAGIC | --- | --- | --- | --- |
# MAGIC | 1 | 2019-07-01 | mobile | 100 |
# MAGIC | 1 | 2019-07-01 | desktop | 100 |
# MAGIC | 2 | 2019-07-01 | mobile | 100 |
# MAGIC | 2 | 2019-07-02 | mobile | 100 |
# MAGIC | 3 | 2019-07-01 | desktop | 100 |
# MAGIC | 3 | 2019-07-02 | desktop | 100 |
# MAGIC
# MAGIC **Output:**
# MAGIC
# MAGIC | spend_date | platform | total_amount | total_users |
# MAGIC | --- | --- | --- | --- |
# MAGIC | 2019-07-01 | both | 200 | 1 |
# MAGIC | 2019-07-01 | mobile | 100 | 1 |
# MAGIC | 2019-07-01 | desktop | 100 | 1 |
# MAGIC | 2019-07-02 | mobile | 100 | 1 |
# MAGIC | 2019-07-02 | desktop | 100 | 1 |
# MAGIC | 2019-07-02 | both | 0 | 0 |
# MAGIC
# MAGIC **Explanation:**
# MAGIC
# MAGIC On `2019-07-01`:
# MAGIC
# MAGIC * User `1` used both platforms, so they contribute `200` to `both`.
# MAGIC * User `2` used only `mobile`, so they contribute `100` to `mobile`.
# MAGIC * User `3` used only `desktop`, so they contribute `100` to `desktop`.
# MAGIC
# MAGIC On `2019-07-02`:
# MAGIC
# MAGIC * User `2` used only `mobile`.
# MAGIC * User `3` used only `desktop`.
# MAGIC * No user used both platforms, so the `both` row has `0` users and `0` amount.