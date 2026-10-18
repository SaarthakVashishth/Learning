# Databricks notebook source
# MAGIC %md
# MAGIC ## 610. Triangle Judgement (Easy)
# MAGIC
# MAGIC ### Table: `Triangle`
# MAGIC
# MAGIC | Column Name | Type |
# MAGIC | --- | --- |
# MAGIC | `x` | `int` |
# MAGIC | `y` | `int` |
# MAGIC | `z` | `int` |
# MAGIC
# MAGIC * (`x`, `y`, `z`) is the primary key.
# MAGIC * Each row stores the lengths of three line segments.
# MAGIC
# MAGIC ### Task
# MAGIC For every row, report whether the three line segments can form a triangle.
# MAGIC
# MAGIC Return the result table in any order.
# MAGIC
# MAGIC ### Example
# MAGIC
# MAGIC **Input:** `Triangle`
# MAGIC
# MAGIC | x | y | z |
# MAGIC | --- | --- | --- |
# MAGIC | 13 | 15 | 30 |
# MAGIC | 10 | 20 | 15 |
# MAGIC
# MAGIC **Output:**
# MAGIC
# MAGIC | x | y | z | triangle |
# MAGIC | --- | --- | --- | --- |
# MAGIC | 13 | 15 | 30 | No |
# MAGIC | 10 | 20 | 15 | Yes |
# MAGIC
# MAGIC **Explanation:**
# MAGIC
# MAGIC * `13`, `15`, and `30` cannot form a triangle because the sum of the two smaller sides is not greater than the largest side.
# MAGIC * `10`, `20`, and `15` satisfy the triangle inequality, so they can form a triangle.