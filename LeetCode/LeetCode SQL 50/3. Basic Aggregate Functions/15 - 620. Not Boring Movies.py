# Databricks notebook source
# MAGIC %md
# MAGIC ## 620. Not Boring Movies (Easy)
# MAGIC
# MAGIC ### Table: `Cinema`
# MAGIC
# MAGIC | Column Name | Type |
# MAGIC | --- | --- |
# MAGIC | `id` | `int` |
# MAGIC | `movie` | `varchar` |
# MAGIC | `description` | `varchar` |
# MAGIC | `rating` | `float` |
# MAGIC
# MAGIC * `id` is the primary key.
# MAGIC * Each row stores information about a movie, its description, and its rating.
# MAGIC * `rating` is a float with `2` decimal places in the range `[0, 10]`.
# MAGIC
# MAGIC ### Task
# MAGIC Report the movies that:
# MAGIC
# MAGIC * have an odd-numbered `id`
# MAGIC * have a `description` that is not `"boring"`
# MAGIC
# MAGIC Return the result table ordered by `rating` in descending order.
# MAGIC
# MAGIC ### Example
# MAGIC
# MAGIC **Input:** `Cinema`
# MAGIC
# MAGIC | id | movie | description | rating |
# MAGIC | --- | --- | --- | --- |
# MAGIC | 1 | War | great 3D | 8.9 |
# MAGIC | 2 | Science | fiction | 8.5 |
# MAGIC | 3 | irish | boring | 6.2 |
# MAGIC | 4 | Ice song | Fantacy | 8.6 |
# MAGIC | 5 | House card | Interesting | 9.1 |
# MAGIC
# MAGIC **Output:**
# MAGIC
# MAGIC | id | movie | description | rating |
# MAGIC | --- | --- | --- | --- |
# MAGIC | 5 | House card | Interesting | 9.1 |
# MAGIC | 1 | War | great 3D | 8.9 |
# MAGIC
# MAGIC **Explanation:**
# MAGIC
# MAGIC * Movies with odd IDs are `1`, `3`, and `5`.
# MAGIC * Movie `3` is excluded because its description is `boring`.
# MAGIC * The remaining movies are ordered by rating in descending order.