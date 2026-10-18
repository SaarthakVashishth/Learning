# Databricks notebook source
# MAGIC %md
# MAGIC ## 585. Investments in 2016 (Medium)
# MAGIC
# MAGIC ### Table: `Insurance`
# MAGIC
# MAGIC | Column Name | Type |
# MAGIC | --- | --- |
# MAGIC | `pid` | `int` |
# MAGIC | `tiv_2015` | `float` |
# MAGIC | `tiv_2016` | `float` |
# MAGIC | `lat` | `float` |
# MAGIC | `lon` | `float` |
# MAGIC
# MAGIC * `pid` is the primary key.
# MAGIC * Each row stores information about one insurance policy.
# MAGIC * `lat` and `lon` are guaranteed to be non-null.
# MAGIC
# MAGIC ### Task
# MAGIC Report the sum of all `tiv_2016` values for policyholders who:
# MAGIC
# MAGIC * have the same `tiv_2015` as at least one other policyholder
# MAGIC * are located in a unique city, meaning their (`lat`, `lon`) pair does not appear for any other policyholder
# MAGIC
# MAGIC Round the result to `2` decimal places.
# MAGIC
# MAGIC ### Example
# MAGIC
# MAGIC **Input:** `Insurance`
# MAGIC
# MAGIC | pid | tiv_2015 | tiv_2016 | lat | lon |
# MAGIC | --- | --- | --- | --- | --- |
# MAGIC | 1 | 10 | 5 | 10 | 10 |
# MAGIC | 2 | 20 | 20 | 20 | 20 |
# MAGIC | 3 | 10 | 30 | 20 | 20 |
# MAGIC | 4 | 10 | 40 | 40 | 40 |
# MAGIC
# MAGIC **Output:**
# MAGIC
# MAGIC | tiv_2016 |
# MAGIC | --- |
# MAGIC | 45.00 |
# MAGIC
# MAGIC **Explanation:**
# MAGIC
# MAGIC * Policies `1` and `4` both have a `tiv_2015` value shared with another policyholder.
# MAGIC * Their locations are unique, so both qualify.
# MAGIC * Policies `2` and `3` share the same location, so neither qualifies.
# MAGIC * The sum is `5 + 40 = 45.00`.