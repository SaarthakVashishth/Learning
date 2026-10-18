# Databricks notebook source
# DBTITLE 1,Cell 1
# MAGIC %md
# MAGIC ## 570. Managers with at Least 5 Direct Reports (Medium)
# MAGIC
# MAGIC ### Table: `Employee`
# MAGIC
# MAGIC | Column Name | Type |
# MAGIC | --- | --- |
# MAGIC | `id` | `int` |
# MAGIC | `name` | `varchar` |
# MAGIC | `department` | `varchar` |
# MAGIC | `managerId` | `int` |
# MAGIC
# MAGIC * `id` is the primary key.
# MAGIC * Each row stores an employee's name, department, and manager ID.
# MAGIC * If `managerId` is `null`, the employee has no manager.
# MAGIC * No employee manages themself.
# MAGIC
# MAGIC ### Task
# MAGIC Find the names of managers who have at least `5` direct reports.
# MAGIC
# MAGIC Return the result table in any order.
# MAGIC
# MAGIC ### Example
# MAGIC
# MAGIC **Input:** `Employee`
# MAGIC
# MAGIC | id | name | department | managerId |
# MAGIC | --- | --- | --- | --- |
# MAGIC | 101 | John | A | null |
# MAGIC | 102 | Dan | A | 101 |
# MAGIC | 103 | James | A | 101 |
# MAGIC | 104 | Amy | A | 101 |
# MAGIC | 105 | Anne | A | 101 |
# MAGIC | 106 | Ron | B | 101 |
# MAGIC
# MAGIC **Output:**
# MAGIC
# MAGIC | name |
# MAGIC | --- |
# MAGIC | John |
# MAGIC
# MAGIC **Explanation:**
# MAGIC
# MAGIC * `John` manages `Dan`, `James`, `Amy`, `Anne`, and `Ron`.
# MAGIC * That gives `John` exactly `5` direct reports, so `John` is included.