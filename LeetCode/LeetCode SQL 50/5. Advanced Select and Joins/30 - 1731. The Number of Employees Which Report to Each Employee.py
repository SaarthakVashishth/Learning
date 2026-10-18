# Databricks notebook source
# MAGIC %md
# MAGIC ## 1731. The Number of Employees Which Report to Each Employee (Easy)
# MAGIC
# MAGIC ### Table: `Employees`
# MAGIC
# MAGIC | Column Name | Type |
# MAGIC | --- | --- |
# MAGIC | `employee_id` | `int` |
# MAGIC | `name` | `varchar` |
# MAGIC | `reports_to` | `int` |
# MAGIC | `age` | `int` |
# MAGIC
# MAGIC * `employee_id` contains unique values.
# MAGIC * Each row stores employee information and the manager they report to.
# MAGIC * If `reports_to` is `null`, the employee does not report to anyone.
# MAGIC * A manager is an employee who has at least one direct report.
# MAGIC
# MAGIC ### Task
# MAGIC Report all managers along with:
# MAGIC
# MAGIC * `employee_id`
# MAGIC * `name`
# MAGIC * the number of employees who report directly to them as `reports_count`
# MAGIC * the average age of their direct reports as `average_age`, rounded to the nearest integer
# MAGIC
# MAGIC Return the result table ordered by `employee_id`.
# MAGIC
# MAGIC ### Example 1
# MAGIC
# MAGIC **Input:** `Employees`
# MAGIC
# MAGIC | employee_id | name | reports_to | age |
# MAGIC | --- | --- | --- | --- |
# MAGIC | 9 | Hercy | null | 43 |
# MAGIC | 6 | Alice | 9 | 41 |
# MAGIC | 4 | Bob | 9 | 36 |
# MAGIC | 2 | Winston | null | 37 |
# MAGIC
# MAGIC **Output:**
# MAGIC
# MAGIC | employee_id | name | reports_count | average_age |
# MAGIC | --- | --- | --- | --- |
# MAGIC | 9 | Hercy | 2 | 39 |
# MAGIC
# MAGIC **Explanation:**
# MAGIC
# MAGIC * `Hercy` has two direct reports: `Alice` and `Bob`.
# MAGIC * Their average age is `(41 + 36) / 2 = 38.5`, which rounds to `39`.
# MAGIC
# MAGIC ### Example 2
# MAGIC
# MAGIC **Input:** `Employees`
# MAGIC
# MAGIC | employee_id | name | reports_to | age |
# MAGIC | --- | --- | --- | --- |
# MAGIC | 1 | Michael | null | 45 |
# MAGIC | 2 | Alice | 1 | 38 |
# MAGIC | 3 | Bob | 1 | 42 |
# MAGIC | 4 | Charlie | 2 | 34 |
# MAGIC | 5 | David | 2 | 40 |
# MAGIC | 6 | Eve | 3 | 37 |
# MAGIC | 7 | Frank | null | 50 |
# MAGIC | 8 | Grace | null | 48 |
# MAGIC
# MAGIC **Output:**
# MAGIC
# MAGIC | employee_id | name | reports_count | average_age |
# MAGIC | --- | --- | --- | --- |
# MAGIC | 1 | Michael | 2 | 40 |
# MAGIC | 2 | Alice | 2 | 37 |
# MAGIC | 3 | Bob | 1 | 37 |
# MAGIC
# MAGIC **Explanation:**
# MAGIC
# MAGIC * `Michael` manages `Alice` and `Bob`, so `reports_count = 2` and average age is `(38 + 42) / 2 = 40`.
# MAGIC * `Alice` manages `Charlie` and `David`, so `reports_count = 2` and average age is `(34 + 40) / 2 = 37`.
# MAGIC * `Bob` manages `Eve`, so `reports_count = 1` and average age is `37`.