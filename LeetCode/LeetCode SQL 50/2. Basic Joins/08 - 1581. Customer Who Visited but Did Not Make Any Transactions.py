# Databricks notebook source
# /// script
# [tool.databricks.environment]
# environment_version = "6"
# ///
# DBTITLE 1,Cell 1
# MAGIC %md
# MAGIC ## 1581. Customer Who Visited but Did Not Make Any Transactions (Easy)
# MAGIC
# MAGIC ### Table: `Visits`
# MAGIC
# MAGIC | Column Name | Type |
# MAGIC | --- | --- |
# MAGIC | `visit_id` | `int` |
# MAGIC | `customer_id` | `int` |
# MAGIC
# MAGIC * `visit_id` contains unique values for this table.
# MAGIC * Each row stores a customer visit to the mall.
# MAGIC
# MAGIC ### Table: `Transactions`
# MAGIC
# MAGIC | Column Name | Type |
# MAGIC | --- | --- |
# MAGIC | `transaction_id` | `int` |
# MAGIC | `visit_id` | `int` |
# MAGIC | `amount` | `int` |
# MAGIC
# MAGIC * `transaction_id` contains unique values for this table.
# MAGIC * Each row stores a transaction made during a visit.
# MAGIC
# MAGIC ### Task
# MAGIC Find the IDs of customers who visited without making any transactions, along with the number of such visits.
# MAGIC
# MAGIC Return the result table in any order.
# MAGIC
# MAGIC ### Example
# MAGIC
# MAGIC **Input:** `Visits`
# MAGIC
# MAGIC | visit_id | customer_id |
# MAGIC | --- | --- |
# MAGIC | 1 | 23 |
# MAGIC | 2 | 9 |
# MAGIC | 4 | 30 |
# MAGIC | 5 | 54 |
# MAGIC | 6 | 96 |
# MAGIC | 7 | 54 |
# MAGIC | 8 | 54 |
# MAGIC
# MAGIC **Input:** `Transactions`
# MAGIC
# MAGIC | transaction_id | visit_id | amount |
# MAGIC | --- | --- | --- |
# MAGIC | 2 | 5 | 310 |
# MAGIC | 3 | 5 | 300 |
# MAGIC | 9 | 5 | 200 |
# MAGIC | 12 | 1 | 910 |
# MAGIC | 13 | 2 | 970 |
# MAGIC
# MAGIC **Output:**
# MAGIC
# MAGIC | customer_id | count_no_trans |
# MAGIC | --- | --- |
# MAGIC | 54 | 2 |
# MAGIC | 30 | 1 |
# MAGIC | 96 | 1 |
# MAGIC
# MAGIC **Explanation:**
# MAGIC
# MAGIC * Customer `23` made a transaction during their visit, so they are excluded.
# MAGIC * Customer `9` also made a transaction during their visit, so they are excluded.
# MAGIC * Customer `30` visited once without making a transaction.
# MAGIC * Customer `54` visited three times, and `2` of those visits had no transactions.
# MAGIC * Customer `96` visited once without making a transaction.

# COMMAND ----------

# DBTITLE 1,Initialisation
import pandas as pd

visits_data = {
                "visit_id": [1,2,4,5,6,7,8],
                "customer_id": [23,9,30,54,96,54,54]
            }

transactions_data = {
                "transaction_id": [2,3,9,12,13],
                "visit_id": [5,5,5,1,2],
                "amount": [310,300,200,910,970]
            }

visits = spark.createDataFrame(pd.DataFrame(visits_data))
transactions = spark.createDataFrame(pd.DataFrame(transactions_data))

visits.createOrReplaceTempView("Visits")
transactions.createOrReplaceTempView("Transactions")

# COMMAND ----------

# DBTITLE 1,SQL
# MAGIC %sql
# MAGIC SELECT
# MAGIC     customer_id
# MAGIC     , COUNT(a.visit_id) AS count_no_trans
# MAGIC FROM
# MAGIC     Visits AS a
# MAGIC LEFT JOIN
# MAGIC     Transactions AS b
# MAGIC ON
# MAGIC     a.visit_id = b.visit_id
# MAGIC WHERE
# MAGIC     transaction_id IS NULL
# MAGIC GROUP BY
# MAGIC     customer_id
# MAGIC ORDER BY
# MAGIC     count_no_trans DESC;

# COMMAND ----------

# DBTITLE 1,PySpark
from pyspark.sql.functions import isnull, count, col

a = visits.alias("a")
b = transactions.alias("b")

result = (a
          .join(b, a["visit_id"] == b["visit_id"], "left")
          .filter(isnull(b["transaction_id"]))
          .groupBy(a["customer_id"])
          .agg(count(a["visit_id"]).alias("no_of_trans"))
          .select(a["customer_id"], "no_of_trans")
          .orderBy(col("no_of_trans").desc())
)

display(result)