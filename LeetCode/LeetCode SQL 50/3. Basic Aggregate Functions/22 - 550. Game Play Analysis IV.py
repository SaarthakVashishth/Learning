# Databricks notebook source
# MAGIC %md
# MAGIC ## 550. Game Play Analysis IV (Medium)
# MAGIC
# MAGIC ### Table: `Activity`
# MAGIC
# MAGIC | Column Name | Type |
# MAGIC | --- | --- |
# MAGIC | `player_id` | `int` |
# MAGIC | `device_id` | `int` |
# MAGIC | `event_date` | `date` |
# MAGIC | `games_played` | `int` |
# MAGIC
# MAGIC * (`player_id`, `event_date`) is the primary key.
# MAGIC * This table records player activity for a game.
# MAGIC * Each row shows a player logging in on a given date using a device and playing some number of games.
# MAGIC
# MAGIC ### Task
# MAGIC Report the fraction of players who logged in again on the day immediately after their first login.
# MAGIC
# MAGIC * Divide the number of players who returned the next day after their first login by the total number of players.
# MAGIC * Round the result to `2` decimal places.
# MAGIC
# MAGIC ### Example
# MAGIC
# MAGIC **Input:** `Activity`
# MAGIC
# MAGIC | player_id | device_id | event_date | games_played |
# MAGIC | --- | --- | --- | --- |
# MAGIC | 1 | 2 | 2016-03-01 | 5 |
# MAGIC | 1 | 2 | 2016-03-02 | 6 |
# MAGIC | 2 | 3 | 2017-06-25 | 1 |
# MAGIC | 3 | 1 | 2016-03-02 | 0 |
# MAGIC | 3 | 4 | 2018-07-03 | 5 |
# MAGIC
# MAGIC **Output:**
# MAGIC
# MAGIC | fraction |
# MAGIC | --- |
# MAGIC | 0.33 |
# MAGIC
# MAGIC **Explanation:**
# MAGIC
# MAGIC * Player `1` logged in again on the day after their first login.
# MAGIC * Players `2` and `3` did not.
# MAGIC * So the fraction is `1 / 3 = 0.33`.