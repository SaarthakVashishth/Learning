# Databricks notebook source
# MAGIC %md
# MAGIC ## 614. Second Degree Follower
# MAGIC
# MAGIC ### Table: `Follow`
# MAGIC
# MAGIC | Column Name | Type |
# MAGIC | --- | --- |
# MAGIC | `followee` | `varchar` |
# MAGIC | `follower` | `varchar` |
# MAGIC
# MAGIC * (`follower`, `followee`) is the primary key.
# MAGIC * In this social network, `follower` follows `followee`.
# MAGIC
# MAGIC ### Task
# MAGIC A second-degree follower is a user who:
# MAGIC
# MAGIC * is followed by at least one user, and
# MAGIC * that follower itself follows at least one other user
# MAGIC
# MAGIC Find:
# MAGIC
# MAGIC * all users who have at least one second-degree follower
# MAGIC * the number of such followers as `num`
# MAGIC
# MAGIC Return the result table ordered by `followee`.
# MAGIC
# MAGIC ### Example
# MAGIC
# MAGIC **Input:** `Follow`
# MAGIC
# MAGIC | followee | follower |
# MAGIC | --- | --- |
# MAGIC | A | B |
# MAGIC | B | C |
# MAGIC | B | D |
# MAGIC | D | E |
# MAGIC
# MAGIC **Output:**
# MAGIC
# MAGIC | followee | num |
# MAGIC | --- | --- |
# MAGIC | B | 1 |
# MAGIC | D | 1 |
# MAGIC
# MAGIC **Explanation:**
# MAGIC
# MAGIC * `B` is followed by `C` and `D`. Among them, `D` is also followed by `E`, so `B` has one second-degree follower.
# MAGIC * `D` is followed by `E`, and `E` participates in the follower chain for `D`, so `D` contributes one qualifying second-degree relationship in the expected result.

# COMMAND ----------

