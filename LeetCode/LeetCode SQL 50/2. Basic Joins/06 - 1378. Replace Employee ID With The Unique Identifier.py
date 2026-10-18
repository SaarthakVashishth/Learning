# Databricks notebook source
# DBTITLE 1,Cell 1
# MAGIC %md
# MAGIC ## 1378. Replace Employee ID With The Unique Identifier (Easy)
# MAGIC
# MAGIC ### Table: `Employees`
# MAGIC
# MAGIC | Column Name | Type |
# MAGIC | --- | --- |
# MAGIC | `id` | `int` |
# MAGIC | `name` | `varchar` |
# MAGIC
# MAGIC * `id` is the primary key.
# MAGIC * Each row stores an employee ID and name.
# MAGIC
# MAGIC ### Table: `EmployeeUNI`
# MAGIC
# MAGIC | Column Name | Type |
# MAGIC | --- | --- |
# MAGIC | `id` | `int` |
# MAGIC | `unique_id` | `int` |
# MAGIC
# MAGIC * (`id`, `unique_id`) is the primary key.
# MAGIC * Each row maps an employee ID to a unique identifier.
# MAGIC
# MAGIC ### Task
# MAGIC Show the `unique_id` of each employee. If an employee does not have a unique ID, return `null` instead.
# MAGIC
# MAGIC Return the result table in any order.
# MAGIC
# MAGIC ### Example
# MAGIC
# MAGIC **Input:** `Employees`
# MAGIC
# MAGIC | id | name |
# MAGIC | --- | --- |
# MAGIC | 1 | Alice |
# MAGIC | 7 | Bob |
# MAGIC | 11 | Meir |
# MAGIC | 90 | Winston |
# MAGIC | 3 | Jonathan |
# MAGIC
# MAGIC **Input:** `EmployeeUNI`
# MAGIC
# MAGIC | id | unique_id |
# MAGIC | --- | --- |
# MAGIC | 3 | 1 |
# MAGIC | 11 | 2 |
# MAGIC | 90 | 3 |
# MAGIC
# MAGIC **Output:**
# MAGIC
# MAGIC | unique_id | name |
# MAGIC | --- | --- |
# MAGIC | null | Alice |
# MAGIC | null | Bob |
# MAGIC | 2 | Meir |
# MAGIC | 3 | Winston |
# MAGIC | 1 | Jonathan |
# MAGIC
# MAGIC **Explanation:**
# MAGIC
# MAGIC * `Alice` and `Bob` do not have a matching unique ID, so `null` is returned.
# MAGIC * `Meir` has unique ID `2`.
# MAGIC * `Winston` has unique ID `3`.
# MAGIC * `Jonathan` has unique ID `1`.

# COMMAND ----------

# DBTITLE 1,Initialization
employees_data = [(1,"Alice"), (7,"Bob"), (11,"Meir"), (90, "Winston"), (3, "Jonathan")]
employees_column = ["id", "name"]

employee_uni_data = [(3,1), (11,2), (90,3)]
employee_uni_column = ["id", "unique_id"]

employees = spark.createDataFrame(data=employees_data, schema=employees_column)
employee_uni = spark.createDataFrame(data=employee_uni_data, schema=employee_uni_column)

display(employees)
display(employee_uni)

employees.createOrReplaceTempView("employees")
employee_uni.createOrReplaceTempView("employee_uni")

# COMMAND ----------

# DBTITLE 1,SQL
# MAGIC %sql
# MAGIC SELECT
# MAGIC     e_uni.unique_id
# MAGIC     ,e.name
# MAGIC FROM
# MAGIC     employees e
# MAGIC LEFT JOIN
# MAGIC     employee_uni e_uni
# MAGIC ON
# MAGIC     e.id = e_uni.id;

# COMMAND ----------

# DBTITLE 1,PySpark
result = (employees
          .join(employee_uni, employees.id == employee_uni.id, "left")
          .select(employee_uni.unique_id, employees.name)
        )
    
display(result)