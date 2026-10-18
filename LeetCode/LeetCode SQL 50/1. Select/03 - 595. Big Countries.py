# Databricks notebook source
# DBTITLE 1,Cell 1
# MAGIC %md
# MAGIC ## 595. Big Countries (Easy)
# MAGIC
# MAGIC ### Table: `World`
# MAGIC
# MAGIC | Column Name | Type |
# MAGIC | --- | --- |
# MAGIC | `name` | `varchar` |
# MAGIC | `continent` | `varchar` |
# MAGIC | `area` | `int` |
# MAGIC | `population` | `int` |
# MAGIC | `gdp` | `bigint` |
# MAGIC
# MAGIC * `name` is the primary key (unique values) for this table.
# MAGIC * Each row contains a country's name, continent, area, population, and GDP.
# MAGIC * A country is considered big if:
# MAGIC   * its `area` is at least `3000000`, or
# MAGIC   * its `population` is at least `25000000`.
# MAGIC
# MAGIC ### Task
# MAGIC Find the `name`, `population`, and `area` of all big countries.
# MAGIC
# MAGIC Return the result table in any order.
# MAGIC
# MAGIC ### Example
# MAGIC
# MAGIC **Input:** `World`
# MAGIC
# MAGIC | name | continent | area | population | gdp |
# MAGIC | --- | --- | --- | --- | --- |
# MAGIC | Afghanistan | Asia | 652230 | 25500100 | 20343000000 |
# MAGIC | Albania | Europe | 28748 | 2831741 | 12960000000 |
# MAGIC | Algeria | Africa | 2381741 | 37100000 | 188681000000 |
# MAGIC | Andorra | Europe | 468 | 78115 | 3712000000 |
# MAGIC | Angola | Africa | 1246700 | 20609294 | 100990000000 |
# MAGIC
# MAGIC **Output:**
# MAGIC
# MAGIC | name | population | area |
# MAGIC | --- | --- | --- |
# MAGIC | Afghanistan | 25500100 | 652230 |
# MAGIC | Algeria | 37100000 | 2381741 |
# MAGIC
# MAGIC **Explanation:**
# MAGIC
# MAGIC * `Afghanistan` qualifies because its population is at least `25000000`.
# MAGIC * `Algeria` qualifies because its population is at least `25000000`.
# MAGIC * The remaining countries do not meet either condition.

# COMMAND ----------

# DBTITLE 1,Initialisation
from pyspark.sql import SparkSession
import pandas as pd
spark = SparkSession.builder.appName("Leet_Select_3").getOrCreate()

# creating df from pandas df
data = {
        "name":["Afghanistan", "Albania", "Algeria", "Andorra", "Angola"]
        ,"continent":["Asia", "Europe", "Africa", "Europe", "Africa"]
        ,"area":[652230, 28748, 2381741, 468, 1246700]
        ,"population":[25500100, 2831741, 37100000, 78115, 20609294]
        ,"gdp":[20343000000, 12960000000, 188681000000, 3712000000, 100990000000]
    }

world = spark.createDataFrame(pd.DataFrame(data))

world.display()
world.createOrReplaceTempView("World")


# COMMAND ----------

# DBTITLE 1,SQL
# MAGIC %sql
# MAGIC SELECT
# MAGIC     name
# MAGIC     , population
# MAGIC     , area
# MAGIC FROM
# MAGIC     World
# MAGIC WHERE
# MAGIC     area >= 3000000
# MAGIC     OR population >= 25000000;

# COMMAND ----------

# DBTITLE 1,PySpark
from pyspark.sql.functions import col

result = (world
          .filter((col("area") >= 3000000) | (col("population") >= 25000000))
          .select("name", "population", "area")
        )

result.display()
