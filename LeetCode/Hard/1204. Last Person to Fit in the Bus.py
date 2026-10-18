# Databricks notebook source
# MAGIC %md
# MAGIC ## 1204. Last Person to Fit in the Bus
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
# MAGIC * `turn` determines the boarding order.
# MAGIC * Only one person can board at a time.
# MAGIC * The bus has a weight limit of `1000` kilograms.
# MAGIC
# MAGIC ### Task
# MAGIC Find the name of the last person who can board the bus without exceeding the weight limit.
# MAGIC
# MAGIC Return the result table in any order.
# MAGIC
# MAGIC ### Example
# MAGIC
# MAGIC **Input:** `Queue`
# MAGIC
# MAGIC | person_id | person_name | weight | turn |
# MAGIC | --- | --- | --- | --- |
# MAGIC | 5 | Alice | 250 | 1 |
# MAGIC | 3 | Bob | 175 | 5 |
# MAGIC | 6 | Alex | 350 | 2 |
# MAGIC | 2 | John Doe | 400 | 3 |
# MAGIC | 4 | Elon Musk | 500 | 4 |
# MAGIC | 1 | Winston | 200 | 6 |
# MAGIC
# MAGIC **Output:**
# MAGIC
# MAGIC | person_name |
# MAGIC | --- |
# MAGIC | John Doe |
# MAGIC
# MAGIC **Explanation:**
# MAGIC
# MAGIC People board in order of `turn`:
# MAGIC
# MAGIC * `Alice` (`250`) → total = `250`
# MAGIC * `Alex` (`350`) → total = `600`
# MAGIC * `John Doe` (`400`) → total = `1000`
# MAGIC * `Elon Musk` (`500`) would exceed the limit, so boarding stops
# MAGIC
# MAGIC Therefore, the last person who can board is `John Doe`.

# COMMAND ----------

