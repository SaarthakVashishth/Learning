# Databricks notebook source
# MAGIC %md
# MAGIC ## 596. Classes With at Least 5 Students (Easy)
# MAGIC
# MAGIC ### Table: `Courses`
# MAGIC
# MAGIC | Column Name | Type |
# MAGIC | --- | --- |
# MAGIC | `student` | `varchar` |
# MAGIC | `class` | `varchar` |
# MAGIC
# MAGIC * (`student`, `class`) is the primary key.
# MAGIC * Each row shows that a student is enrolled in a class.
# MAGIC
# MAGIC ### Task
# MAGIC Find all classes that have at least `5` students.
# MAGIC
# MAGIC Return the result table in any order.
# MAGIC
# MAGIC ### Example
# MAGIC
# MAGIC **Input:** `Courses`
# MAGIC
# MAGIC | student | class |
# MAGIC | --- | --- |
# MAGIC | A | Math |
# MAGIC | B | English |
# MAGIC | C | Math |
# MAGIC | D | Biology |
# MAGIC | E | Math |
# MAGIC | F | Computer |
# MAGIC | G | Math |
# MAGIC | H | Math |
# MAGIC | I | Math |
# MAGIC
# MAGIC **Output:**
# MAGIC
# MAGIC | class |
# MAGIC | --- |
# MAGIC | Math |
# MAGIC
# MAGIC **Explanation:**
# MAGIC
# MAGIC * `Math` has `6` students, so it is included.
# MAGIC * `English`, `Biology`, and `Computer` each have only `1` student, so they are excluded.