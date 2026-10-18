# Databricks notebook source
# MAGIC %md
# MAGIC ## 1204. Last Person to Fit in the Bus (Medium)
# MAGIC
# MAGIC ### Table: `Queue`
# MAGIC
# MAGIC | Column Name | Type |
# MAGIC | --- | --- |
# MAGIC | `person_id` | `int` |
# MAGIC | `person_name` | `varchar` |
# MAGIC | `weight` | `int` |
# MAGIC | `turn` | `int` |
# MAGIC
# MAGIC * `person_id` contains unique values.
# MAGIC * This table stores people waiting to board a bus.
# MAGIC * `person_id` and `turn` contain all numbers from `1` to `n`.
# MAGIC * `turn` defines boarding order, where `1` boards first.
# MAGIC * `weight` is measured in kilograms.
# MAGIC
# MAGIC ### Task
# MAGIC Find the `person_name` of the last person who can board the bus without exceeding the weight limit of `1000` kilograms.
# MAGIC
# MAGIC * The first person is guaranteed not to exceed the limit.
# MAGIC * Only one person boards at each turn.
# MAGIC
# MAGIC ### Example
# MAGIC
# MAGIC **Input:** `Queue`
# MAGIC
# MAGIC | person_id | person_name | weight | turn |
# MAGIC | --- | --- | --- | --- |
# MAGIC | 5 | Alice | 250 | 1 |
# MAGIC | 4 | Bob | 175 | 5 |
# MAGIC | 3 | Alex | 350 | 2 |
# MAGIC | 6 | John Cena | 400 | 3 |
# MAGIC | 1 | Winston | 500 | 6 |
# MAGIC | 2 | Marie | 200 | 4 |
# MAGIC
# MAGIC **Output:**
# MAGIC
# MAGIC | person_name |
# MAGIC | --- |
# MAGIC | John Cena |
# MAGIC
# MAGIC **Explanation:**
# MAGIC
# MAGIC * After `Alice`, the total weight is `250`.
# MAGIC * After `Alex`, the total weight is `600`.
# MAGIC * After `John Cena`, the total weight is `1000`, so he can still board.
# MAGIC * `Marie` would raise the total to `1200`, so she cannot board.
# MAGIC * Therefore, `John Cena` is the last person who fits.