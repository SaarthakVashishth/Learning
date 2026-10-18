# Databricks notebook source
# MAGIC %md
# MAGIC ## 1789. Primary Department for Each Employee (Easy)
# MAGIC
# MAGIC ### Table: `Employee`
# MAGIC
# MAGIC | Column Name | Type |
# MAGIC | --- | --- |
# MAGIC | `employee_id` | `int` |
# MAGIC | `department_id` | `int` |
# MAGIC | `primary_flag` | `varchar` |
# MAGIC
# MAGIC * (`employee_id`, `department_id`) is the primary key.
# MAGIC * `primary_flag` is an enum with values `Y` and `N`.
# MAGIC * If `primary_flag = 'Y'`, that department is the employee's primary department.
# MAGIC * If an employee belongs to only one department, that department should be returned even if `primary_flag = 'N'`.
# MAGIC
# MAGIC ### Task
# MAGIC Report each employee with their primary department.
# MAGIC
# MAGIC Return the result table in any order.
# MAGIC
# MAGIC ### Example
# MAGIC
# MAGIC **Input:** `Employee`
# MAGIC
# MAGIC | employee_id | department_id | primary_flag |
# MAGIC | --- | --- | --- |
# MAGIC | 1 | 1 | N |
# MAGIC | 2 | 1 | Y |
# MAGIC | 2 | 2 | N |
# MAGIC | 3 | 3 | N |
# MAGIC | 4 | 2 | N |
# MAGIC | 4 | 3 | Y |
# MAGIC | 4 | 4 | N |
# MAGIC
# MAGIC **Output:**
# MAGIC
# MAGIC | employee_id | department_id |
# MAGIC | --- | --- |
# MAGIC | 1 | 1 |
# MAGIC | 2 | 1 |
# MAGIC | 3 | 3 |
# MAGIC | 4 | 3 |
# MAGIC
# MAGIC **Explanation:**
# MAGIC
# MAGIC * Employee `1` belongs to only one department, so department `1` is returned.
# MAGIC * Employee `2` has primary department `1` because `primary_flag = 'Y'` there.
# MAGIC * Employee `3` belongs to only one department, so department `3` is returned.
# MAGIC * Employee `4` has primary department `3`.