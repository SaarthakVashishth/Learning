# Databricks notebook source
# MAGIC %md
# MAGIC ## 1194. Tournament Winners
# MAGIC
# MAGIC ### Table: `Players`
# MAGIC
# MAGIC | Column Name | Type |
# MAGIC | --- | --- |
# MAGIC | `player_id` | `int` |
# MAGIC | `group_id` | `int` |
# MAGIC
# MAGIC * Each player belongs to a group.
# MAGIC
# MAGIC ### Table: `Matches`
# MAGIC
# MAGIC | Column Name | Type |
# MAGIC | --- | --- |
# MAGIC | `match_id` | `int` |
# MAGIC | `first_player` | `int` |
# MAGIC | `second_player` | `int` |
# MAGIC | `first_score` | `int` |
# MAGIC | `second_score` | `int` |
# MAGIC
# MAGIC * Each match is played between two players.
# MAGIC * Points are assigned as follows:
# MAGIC   * winner gets `3` points
# MAGIC   * draw gives both players `1` point
# MAGIC   * loser gets `0` points
# MAGIC
# MAGIC ### Task
# MAGIC Find the winner in each group.
# MAGIC
# MAGIC If multiple players in the same group have the highest number of points, return the player with the smallest `player_id`.
# MAGIC
# MAGIC ### Example
# MAGIC
# MAGIC **Input:** `Players`
# MAGIC
# MAGIC | player_id | group_id |
# MAGIC | --- | --- |
# MAGIC | 15 | 1 |
# MAGIC | 25 | 1 |
# MAGIC | 30 | 1 |
# MAGIC | 45 | 1 |
# MAGIC
# MAGIC **Input:** `Matches`
# MAGIC
# MAGIC | match_id | first_player | second_player | first_score | second_score |
# MAGIC | --- | --- | --- | --- | --- |
# MAGIC | 1 | 15 | 45 | 3 | 0 |
# MAGIC | 2 | 30 | 25 | 1 | 2 |
# MAGIC | 3 | 15 | 30 | 2 | 2 |
# MAGIC | 4 | 45 | 25 | 1 | 1 |
# MAGIC
# MAGIC **Output:**
# MAGIC
# MAGIC | group_id | player_id |
# MAGIC | --- | --- |
# MAGIC | 1 | 15 |
# MAGIC
# MAGIC **Explanation:**
# MAGIC
# MAGIC Points by player:
# MAGIC
# MAGIC * Player `15` → `3 + 1 = 4`
# MAGIC * Player `25` → `3 + 1 = 4`
# MAGIC * Player `30` → `1`
# MAGIC * Player `45` → `1`
# MAGIC
# MAGIC Players `15` and `25` tie with the highest points, so return the smaller `player_id`, which is `15`.

# COMMAND ----------

