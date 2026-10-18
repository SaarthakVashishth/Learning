# Databricks notebook source
# MAGIC %md
# MAGIC ## 1978. Employees Whose Manager Left the Company (Easy)
# MAGIC
# MAGIC ### Table: `Employees`
# MAGIC
# MAGIC | Column Name | Type |
# MAGIC | --- | --- |
# MAGIC | `employee_id` | `int` |
# MAGIC | `name` | `varchar` |
# MAGIC | `manager_id` | `int` |
# MAGIC | `salary` | `int` |
# MAGIC
# MAGIC * `employee_id` is the primary key.
# MAGIC * Each row stores employee information, salary, and manager ID.
# MAGIC * If `manager_id` is `null`, the employee has no manager.
# MAGIC * If a manager leaves the company, their row is deleted but their reports may still reference that `manager_id`.
# MAGIC
# MAGIC ### Task
# MAGIC Find the IDs of employees who:
# MAGIC
# MAGIC * have a salary strictly less than `30000`
# MAGIC * have a manager who left the company
# MAGIC
# MAGIC Return the result table ordered by `employee_id`.
# MAGIC
# MAGIC ### Example
# MAGIC
# MAGIC **Input:** `Employees`
# MAGIC
# MAGIC | employee_id | name | manager_id | salary |
# MAGIC | --- | --- | --- | --- |
# MAGIC | 3 | Mila | 9 | 60301 |
# MAGIC | 12 | Antonella | null | 31000 |
# MAGIC | 13 | Emery | null | 67084 |
# MAGIC | 1 | Kalel | 11 | 21241 |
# MAGIC | 9 | Mikaela | null | 50937 |
# MAGIC | 11 | Joziah | 6 | 28485 |
# MAGIC
# MAGIC **Output:**
# MAGIC
# MAGIC | employee_id |
# MAGIC | --- |
# MAGIC | 11 |
# MAGIC
# MAGIC **Explanation:**
# MAGIC
# MAGIC * Employees with salary less than `30000` are `1` and `11`.
# MAGIC * Employee `1` reports to employee `11`, who is still in the table, so `1` is excluded.
# MAGIC * Employee `11` reports to manager `6`, whose row is missing, so `11` is included.