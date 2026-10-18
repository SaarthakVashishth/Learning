# Databricks notebook source
# MAGIC %md
# MAGIC ## 1757. Recyclable and Low Fat Products (Easy)
# MAGIC
# MAGIC ### Table: `Products`
# MAGIC
# MAGIC | Column Name | Type |
# MAGIC | --- | --- |
# MAGIC | `product_id` | `int` |
# MAGIC | `low_fats` | `enum` |
# MAGIC | `recyclable` | `enum` |
# MAGIC
# MAGIC * `product_id` is the primary key (unique values) for this table.
# MAGIC * `low_fats` is an enum with values `('Y', 'N')`, where `Y` means the product is low fat and `N` means it is not.
# MAGIC * `recyclable` is an enum with values `('Y', 'N')`, where `Y` means the product is recyclable and `N` means it is not.
# MAGIC
# MAGIC ### Task
# MAGIC Find the IDs of products that are both:
# MAGIC * low fat
# MAGIC * recyclable
# MAGIC
# MAGIC Return the result table in any order.
# MAGIC
# MAGIC ### Example
# MAGIC
# MAGIC **Input:** `Products`
# MAGIC
# MAGIC | product_id | low_fats | recyclable |
# MAGIC | --- | --- | --- |
# MAGIC | 0 | Y | N |
# MAGIC | 1 | Y | Y |
# MAGIC | 2 | N | Y |
# MAGIC | 3 | Y | Y |
# MAGIC | 4 | N | N |
# MAGIC
# MAGIC **Output:**
# MAGIC
# MAGIC | product_id |
# MAGIC | --- |
# MAGIC | 1 |
# MAGIC | 3 |
# MAGIC
# MAGIC **Explanation:** Only products `1` and `3` are both low fat and recyclable.
# MAGIC
# MAGIC

# COMMAND ----------

# DBTITLE 1,Initialisation
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("Leet_Select_1").getOrCreate()

data = [(0,"Y","N"), (1,"Y","Y"), (2,"N","Y"), (3,"Y","Y"), (4,"N","N")]
products = spark.createDataFrame(data, schema=["product_id", "low_fats", "recyclable"])

products.display()
products.createOrReplaceTempView("Products")

# COMMAND ----------

# DBTITLE 1,SQL
# MAGIC %sql
# MAGIC SELECT
# MAGIC     product_id
# MAGIC FROM
# MAGIC     Products
# MAGIC WHERE
# MAGIC     low_fats = 'Y'
# MAGIC     AND recyclable = 'Y';

# COMMAND ----------

# DBTITLE 1,PySpark
from pyspark.sql.functions import col

result = (products
            .filter((col("low_fats") == "Y") & (col("recyclable") == "Y"))
            .select("product_id")
        )

result.display()