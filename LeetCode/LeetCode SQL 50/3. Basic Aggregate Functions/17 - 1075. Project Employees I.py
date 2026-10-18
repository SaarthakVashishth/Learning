# Databricks notebook source
# MAGIC %md
# MAGIC ## 1075. Project Employees I (Easy)
# MAGIC
# MAGIC ### Table: `Project`
# MAGIC
# MAGIC | Column Name | Type |
# MAGIC | --- | --- |
# MAGIC | `project_id` | `int` |
# MAGIC | `employee_id` | `int` |
# MAGIC
# MAGIC * (`project_id`, `employee_id`) is the primary key.
# MAGIC * `employee_id` is a foreign key referencing `Employee`.
# MAGIC * Each row shows an employee working on a project.
# MAGIC
# MAGIC ### Table: `Employee`
# MAGIC
# MAGIC | Column Name | Type |
# MAGIC | --- | --- |
# MAGIC | `employee_id` | `int` |
# MAGIC | `name` | `varchar` |
# MAGIC | `experience_years` | `int` |
# MAGIC
# MAGIC * `employee_id` is the primary key.
# MAGIC * `experience_years` is guaranteed to be non-null.
# MAGIC * Each row stores information about one employee.
# MAGIC
# MAGIC ### Task
# MAGIC Report the average experience years of employees for each project.
# MAGIC
# MAGIC * Return the average as `average_years`.
# MAGIC * Round the result to `2` decimal places.
# MAGIC
# MAGIC Return the result table in any order.
# MAGIC
# MAGIC ### Example
# MAGIC
# MAGIC **Input:** `Project`
# MAGIC
# MAGIC | project_id | employee_id |
# MAGIC | --- | --- |
# MAGIC | 1 | 1 |
# MAGIC | 1 | 2 |
# MAGIC | 1 | 3 |
# MAGIC | 2 | 1 |
# MAGIC | 2 | 4 |
# MAGIC
# MAGIC **Input:** `Employee`
# MAGIC
# MAGIC | employee_id | name | experience_years |
# MAGIC | --- | --- | --- |
# MAGIC | 1 | Khaled | 3 |
# MAGIC | 2 | Ali | 2 |
# MAGIC | 3 | John | 1 |
# MAGIC | 4 | Doe | 2 |
# MAGIC
# MAGIC **Output:**
# MAGIC
# MAGIC | project_id | average_years |
# MAGIC | --- | --- |
# MAGIC | 1 | 2.00 |
# MAGIC | 2 | 2.50 |
# MAGIC
# MAGIC **Explanation:**
# MAGIC
# MAGIC * Project `1` has employees with `3`, `2`, and `1` years of experience, so the average is `2.00`.
# MAGIC * Project `2` has employees with `3` and `2` years of experience, so the average is `2.50`.