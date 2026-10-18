# Databricks notebook source
# /// script
# [tool.databricks.environment]
# environment_version = "6"
# ///
# DBTITLE 1,Cell 1
# MAGIC %md
# MAGIC ## 577. Employee Bonus (Easy)
# MAGIC
# MAGIC ### Table: `Employee`
# MAGIC
# MAGIC | Column Name | Type |
# MAGIC | --- | --- |
# MAGIC | `empId` | `int` |
# MAGIC | `name` | `varchar` |
# MAGIC | `supervisor` | `int` |
# MAGIC | `salary` | `int` |
# MAGIC
# MAGIC * `empId` contains unique values for this table.
# MAGIC * Each row stores an employee's ID, name, supervisor ID, and salary.
# MAGIC
# MAGIC ### Table: `Bonus`
# MAGIC
# MAGIC | Column Name | Type |
# MAGIC | --- | --- |
# MAGIC | `empId` | `int` |
# MAGIC | `bonus` | `int` |
# MAGIC
# MAGIC * `empId` contains unique values for this table.
# MAGIC * `empId` is a foreign key referencing `Employee`.
# MAGIC * Each row stores an employee's bonus amount.
# MAGIC
# MAGIC ### Task
# MAGIC Report the `name` and `bonus` of each employee who satisfies at least one of these conditions:
# MAGIC
# MAGIC * the bonus is less than `1000`
# MAGIC * the employee did not receive a bonus
# MAGIC
# MAGIC Return the result table in any order.
# MAGIC
# MAGIC ### Example
# MAGIC
# MAGIC **Input:** `Employee`
# MAGIC
# MAGIC | empId | name | supervisor | salary |
# MAGIC | --- | --- | --- | --- |
# MAGIC | 3 | Brad | null | 4000 |
# MAGIC | 1 | John | 3 | 1000 |
# MAGIC | 2 | Dan | 3 | 2000 |
# MAGIC | 4 | Thomas | 3 | 4000 |
# MAGIC
# MAGIC **Input:** `Bonus`
# MAGIC
# MAGIC | empId | bonus |
# MAGIC | --- | --- |
# MAGIC | 2 | 500 |
# MAGIC | 4 | 2000 |
# MAGIC
# MAGIC **Output:**
# MAGIC
# MAGIC | name | bonus |
# MAGIC | --- | --- |
# MAGIC | Brad | null |
# MAGIC | John | null |
# MAGIC | Dan | 500 |
# MAGIC
# MAGIC **Explanation:**
# MAGIC
# MAGIC * `Brad` and `John` have no matching bonus record, so their bonus is `null`.
# MAGIC * `Dan` has a bonus of `500`, which is less than `1000`.
# MAGIC * `Thomas` has a bonus of `2000`, so `Thomas` is excluded.

# COMMAND ----------

# DBTITLE 1,Initialization
emp_data = [
    (3, "Brad", None, 400)
    ,(1, "John", 3, 1000)
    , (2, "Dan", 3, 2000)
    , (4, "Thomas", 3, 4000)
]

bonus_data = [
    (2, 500)
    , (4, 2000)
]

employee = spark.createDataFrame(emp_data, ["empId", "name", "supervisor", "salary"])
bonus = spark.createDataFrame(bonus_data, ["empId", "bonus"])

employee.createTempView("Employee")
bonus.createTempView("Bonus")

# COMMAND ----------

# DBTITLE 1,SQL
# MAGIC %sql
# MAGIC SELECT
# MAGIC     a.name
# MAGIC     , b.bonus
# MAGIC FROM
# MAGIC     Employee a
# MAGIC LEFT JOIN
# MAGIC     Bonus b
# MAGIC ON
# MAGIC     a.empId = b.empId
# MAGIC WHERE
# MAGIC     b.bonus IS NULL
# MAGIC OR
# MAGIC     b.bonus < 1000;

# COMMAND ----------

# DBTITLE 1,PySpark
from pyspark.sql.functions import isnull, col

result = (employee
          .join(bonus, employee["empId"]==bonus["empId"], "left")
          .filter(isnull("bonus") | (col("bonus") < 1000))
          .select("name", "bonus")
)

display(result)