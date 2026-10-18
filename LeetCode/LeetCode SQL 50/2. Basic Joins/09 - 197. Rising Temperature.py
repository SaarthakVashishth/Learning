# Databricks notebook source
# DBTITLE 1,Cell 1
# MAGIC %md
# MAGIC ## 197. Rising Temperature (Easy)
# MAGIC
# MAGIC ### Table: `Weather`
# MAGIC
# MAGIC | Column Name | Type |
# MAGIC | --- | --- |
# MAGIC | `id` | `int` |
# MAGIC | `recordDate` | `date` |
# MAGIC | `temperature` | `int` |
# MAGIC
# MAGIC * `id` contains unique values for this table.
# MAGIC * There are no two rows with the same `recordDate`.
# MAGIC * Each row stores the temperature recorded on a specific date.
# MAGIC
# MAGIC ### Task
# MAGIC Find the IDs of days whose temperature is higher than the previous day.
# MAGIC
# MAGIC Return the result table in any order.
# MAGIC
# MAGIC ### Example
# MAGIC
# MAGIC **Input:** `Weather`
# MAGIC
# MAGIC | id | recordDate | temperature |
# MAGIC | --- | --- | --- |
# MAGIC | 1 | 2015-01-01 | 10 |
# MAGIC | 2 | 2015-01-02 | 25 |
# MAGIC | 3 | 2015-01-03 | 20 |
# MAGIC | 4 | 2015-01-04 | 30 |
# MAGIC
# MAGIC **Output:**
# MAGIC
# MAGIC | id |
# MAGIC | --- |
# MAGIC | 2 |
# MAGIC | 4 |
# MAGIC
# MAGIC **Explanation:**
# MAGIC
# MAGIC * On `2015-01-02`, the temperature increased from `10` to `25` compared to the previous day.
# MAGIC * On `2015-01-04`, the temperature increased from `20` to `30` compared to the previous day.

# COMMAND ----------

# DBTITLE 1,initialisation
from pyspark.sql.types import StructType, StructField, IntegerType, DateType
from datetime import date

weather_data = [
                [1, date(2015, 1, 1), 10], [2, date(2015, 1, 2), 25], [3, date(2015, 1, 3), 20], [4, date(2015, 1, 4), 30]
            ]
schema = StructType([
            StructField("id", IntegerType(), False),
            StructField("recordDate", DateType(), True),
            StructField("temperature", IntegerType(), True)
        ])

weather = spark.createDataFrame(weather_data, schema)

display(weather)

weather.createOrReplaceTempView("Weather")

# COMMAND ----------

# DBTITLE 1,SQL
# MAGIC %sql
# MAGIC SELECT
# MAGIC     a.id
# MAGIC FROM
# MAGIC     Weather a
# MAGIC JOIN
# MAGIC     Weather b
# MAGIC ON
# MAGIC     a.recordDate = date_add(b.recordDate, 1)
# MAGIC     AND a.temperature > b.temperature;

# COMMAND ----------

# DBTITLE 1,PySpark
from pyspark.sql.functions import date_add

a = weather.alias("a")
b = weather.alias("b")

result = (a
          .join(b,
            (a["recordDate"] == date_add(b["recordDate"], 1)) & 
            (a["temperature"] > b["temperature"]),
            "inner")
          .select(a["id"])
        )

display(result)

# COMMAND ----------

# DBTITLE 1,PySpark Window
from pyspark.sql import Window
from pyspark.sql.functions import lag

windowSpec = Window.partitionBy().orderBy("recordDate")

result = (weather
          .select("id", "recordDate", "temperature", lag("temperature", 1).over(windowSpec).alias("prevDayTemperature"))
          .filter("temperature > prevDayTemperature")
          .select("id")
        )

display(result)