# Databricks notebook source
# MAGIC %md
# MAGIC ## 185. Department Top Three Salaries (Hard)
# MAGIC
# MAGIC ### Table: `Employee`
# MAGIC
# MAGIC | Column Name | Type |
# MAGIC | --- | --- |
# MAGIC | `id` | `int` |
# MAGIC | `name` | `varchar` |
# MAGIC | `salary` | `int` |
# MAGIC | `departmentId` | `int` |
# MAGIC
# MAGIC * `id` is the primary key.
# MAGIC * `departmentId` is a foreign key referencing `Department.id`.
# MAGIC * Each row stores an employee's name, salary, and department.
# MAGIC
# MAGIC ### Table: `Department`
# MAGIC
# MAGIC | Column Name | Type |
# MAGIC | --- | --- |
# MAGIC | `id` | `int` |
# MAGIC | `name` | `varchar` |
# MAGIC
# MAGIC * `id` is the primary key.
# MAGIC * Each row stores one department.
# MAGIC
# MAGIC ### Task
# MAGIC Find the employees who are high earners in each department.
# MAGIC
# MAGIC A high earner is an employee whose salary is in the top `3` unique salaries of their department.
# MAGIC
# MAGIC Return the result table in any order.
# MAGIC
# MAGIC ### Example
# MAGIC
# MAGIC **Input:** `Employee`
# MAGIC
# MAGIC | id | name | salary | departmentId |
# MAGIC | --- | --- | --- | --- |
# MAGIC | 1 | Joe | 85000 | 1 |
# MAGIC | 2 | Henry | 80000 | 2 |
# MAGIC | 3 | Sam | 60000 | 2 |
# MAGIC | 4 | Max | 90000 | 1 |
# MAGIC | 5 | Janet | 69000 | 1 |
# MAGIC | 6 | Randy | 85000 | 1 |
# MAGIC | 7 | Will | 70000 | 1 |
# MAGIC
# MAGIC **Input:** `Department`
# MAGIC
# MAGIC | id | name |
# MAGIC | --- | --- |
# MAGIC | 1 | IT |
# MAGIC | 2 | Sales |
# MAGIC
# MAGIC **Output:**
# MAGIC
# MAGIC | Department | Employee | Salary |
# MAGIC | --- | --- | --- |
# MAGIC | IT | Max | 90000 |
# MAGIC | IT | Joe | 85000 |
# MAGIC | IT | Randy | 85000 |
# MAGIC | IT | Will | 70000 |
# MAGIC | Sales | Henry | 80000 |
# MAGIC | Sales | Sam | 60000 |
# MAGIC
# MAGIC **Explanation:**
# MAGIC
# MAGIC * In `IT`, the top three unique salaries are `90000`, `85000`, and `70000`, so `Max`, `Joe`, `Randy`, and `Will` are included.
# MAGIC * In `Sales`, the top salaries are `80000` and `60000`, so `Henry` and `Sam` are included.