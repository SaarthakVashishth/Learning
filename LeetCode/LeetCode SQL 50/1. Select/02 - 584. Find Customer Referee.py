# Databricks notebook source
# DBTITLE 1,Cell 1
# MAGIC %md
# MAGIC ## 584. Find Customer Referee (Easy)
# MAGIC
# MAGIC ### Table: `Customer`
# MAGIC
# MAGIC | Column Name | Type |
# MAGIC | --- | --- |
# MAGIC | `id` | `int` |
# MAGIC | `name` | `varchar` |
# MAGIC | `referee_id` | `int` |
# MAGIC
# MAGIC * `id` is the primary key for this table.
# MAGIC * Each row stores a customer's ID, name, and the ID of the customer who referred them.
# MAGIC
# MAGIC ### Task
# MAGIC Find the names of customers who are either:
# MAGIC
# MAGIC * referred by a customer with `id != 2`
# MAGIC * not referred by any customer
# MAGIC
# MAGIC Return the result table in any order.
# MAGIC
# MAGIC ### Example
# MAGIC
# MAGIC **Input:** `Customer`
# MAGIC
# MAGIC | id | name | referee_id |
# MAGIC | --- | --- | --- |
# MAGIC | 1 | Will | null |
# MAGIC | 2 | Jane | null |
# MAGIC | 3 | Alex | 2 |
# MAGIC | 4 | Bill | null |
# MAGIC | 5 | Zack | 1 |
# MAGIC | 6 | Mark | 2 |
# MAGIC
# MAGIC **Output:**
# MAGIC
# MAGIC | name |
# MAGIC | --- |
# MAGIC | Will |
# MAGIC | Jane |
# MAGIC | Bill |
# MAGIC | Zack |
# MAGIC
# MAGIC **Explanation:**
# MAGIC
# MAGIC * `Will`, `Jane`, and `Bill` were not referred by any customer.
# MAGIC * `Zack` was referred by customer `1`, which is not `2`.
# MAGIC * `Alex` and `Mark` were referred by customer `2`, so they are excluded.

# COMMAND ----------

# DBTITLE 1,Initialisation
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("Leet_Select_2").getOrCreate()

data = [[1,"Will",None], [2,"Jane",None], [3,"Alex",2], [4,"Bill",None], [5,"Zack",1], [6,"Mark",2]]
columns = ["id", "name", "referee_id"]
customer = spark.createDataFrame(data, columns)

customer.display()
customer.createOrReplaceTempView("Customer")


# COMMAND ----------

# DBTITLE 1,SQL
# MAGIC %sql
# MAGIC SELECT
# MAGIC     name
# MAGIC FROM
# MAGIC     Customer
# MAGIC WHERE
# MAGIC     referee_id <> 2
# MAGIC     OR referee_id IS NULL;

# COMMAND ----------

# DBTITLE 1,PySpark
from pyspark.sql.functions import col

result = (customer
          .filter((col("referee_id") != 2) | col("referee_id").isNull())
          .select("name")
        )
result.display()