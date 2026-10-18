# Databricks notebook source
# DBTITLE 1,Cell 1
# MAGIC %md
# MAGIC ## 1661. Average Time of Process per Machine (Easy)
# MAGIC
# MAGIC ### Table: `Activity`
# MAGIC
# MAGIC | Column Name | Type |
# MAGIC | --- | --- |
# MAGIC | `machine_id` | `int` |
# MAGIC | `process_id` | `int` |
# MAGIC | `activity_type` | `enum` |
# MAGIC | `timestamp` | `float` |
# MAGIC
# MAGIC * (`machine_id`, `process_id`, `activity_type`) is the primary key.
# MAGIC * `machine_id` identifies a machine.
# MAGIC * `process_id` identifies a process running on a machine.
# MAGIC * `activity_type` is either `start` or `end`.
# MAGIC * For every (`machine_id`, `process_id`) pair, the `start` timestamp is earlier than the `end` timestamp.
# MAGIC * Every process has exactly one `start` and one `end` record.
# MAGIC
# MAGIC ### Task
# MAGIC Compute the average time each machine takes to complete a process.
# MAGIC
# MAGIC * Processing time for a process is `end - start`.
# MAGIC * Average processing time is the total processing time for the machine divided by the number of processes run on that machine.
# MAGIC * Return the result as `processing_time`, rounded to `3` decimal places.
# MAGIC
# MAGIC Return the result table in any order.
# MAGIC
# MAGIC ### Example
# MAGIC
# MAGIC **Input:** `Activity`
# MAGIC
# MAGIC | machine_id | process_id | activity_type | timestamp |
# MAGIC | --- | --- | --- | --- |
# MAGIC | 0 | 0 | start | 0.712 |
# MAGIC | 0 | 0 | end | 1.520 |
# MAGIC | 0 | 1 | start | 3.140 |
# MAGIC | 0 | 1 | end | 4.120 |
# MAGIC | 1 | 0 | start | 0.550 |
# MAGIC | 1 | 0 | end | 1.550 |
# MAGIC | 1 | 1 | start | 0.430 |
# MAGIC | 1 | 1 | end | 1.420 |
# MAGIC | 2 | 0 | start | 4.100 |
# MAGIC | 2 | 0 | end | 4.512 |
# MAGIC | 2 | 1 | start | 2.500 |
# MAGIC | 2 | 1 | end | 5.000 |
# MAGIC
# MAGIC **Output:**
# MAGIC
# MAGIC | machine_id | processing_time |
# MAGIC | --- | --- |
# MAGIC | 0 | 0.894 |
# MAGIC | 1 | 0.995 |
# MAGIC | 2 | 1.456 |
# MAGIC
# MAGIC **Explanation:**
# MAGIC
# MAGIC * Machine `0`: `((1.520 - 0.712) + (4.120 - 3.140)) / 2 = 0.894`
# MAGIC * Machine `1`: `((1.550 - 0.550) + (1.420 - 0.430)) / 2 = 0.995`
# MAGIC * Machine `2`: `((4.512 - 4.100) + (5.000 - 2.500)) / 2 = 1.456`

# COMMAND ----------

# DBTITLE 1,Initialisation
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("AverageTimeOfProcess").getOrCreate()

activity_data = [
    [0, 0, "start", 0.712],
    [0, 0, "end", 1.520],
    [0, 1, "start", 3.140],
    [0, 1, "end", 4.120],
    [1, 0, "start", 0.550],
    [1, 0, "end", 1.550],
    [1, 1, "start", 0.430],
    [1, 1, "end", 1.420],
    [2, 0, "start", 4.100],
    [2, 0, "end", 4.512],
    [2, 1, "start", 2.500],
    [2, 1, "end", 5.000]
]

activity_columns = ["machine_id", "process_id", "activity_type", "timestamp"]

activity = spark.createDataFrame(activity_data, activity_columns)

display(activity)

activity.createOrReplaceTempView("Activity")

# COMMAND ----------

# DBTITLE 1,SQL
# MAGIC %sql
# MAGIC SELECT
# MAGIC     a.machine_id
# MAGIC     , ROUND(SUM(b.timestamp - a.timestamp)/COUNT(*), 3) AS processing_time
# MAGIC FROM
# MAGIC     Activity AS a
# MAGIC JOIN
# MAGIC     Activity AS b
# MAGIC ON
# MAGIC     a.machine_id = b.machine_id
# MAGIC     AND a.process_id = b.process_id
# MAGIC     AND a.activity_type = 'start'
# MAGIC     AND b.activity_type = 'end'
# MAGIC GROUP BY
# MAGIC     a.machine_id;
# MAGIC

# COMMAND ----------

# DBTITLE 1,PySpark
from pyspark.sql.functions import col, when, sum, countDistinct, round

result_df = (activity
            .withColumn("adjusted_timestamp",
                when(col("activity_type") == "start", col("timestamp")*(-1))
            .otherwise(col("timestamp"))
            )
         )

result = (result_df
         .groupBy("machine_id")
         .agg(
            round(sum("adjusted_timestamp") / countDistinct("process_id"), 3).alias("processing_time")
         )
         .select("machine_id", "processing_time")
      )

display(result)

# COMMAND ----------

# DBTITLE 1,PySpark Join
from pyspark.sql.functions import col, sum, round, isnotnull, count

result = (activity.alias("a")
            .join(activity.alias("b")
            , (col("a.machine_id") == col("b.machine_id")) & (col("a.process_id") == col("b.process_id")) & (col("a.activity_type") == "start") & (col("b.activity_type") == "end")
            , "inner")
            .groupBy(col("a.machine_id"))
            .agg(round(sum(col("b.timestamp")-col("a.timestamp"))/count("*"), 3).alias("processing_time"))
            .select("machine_id", "processing_time")
        )

display(result)