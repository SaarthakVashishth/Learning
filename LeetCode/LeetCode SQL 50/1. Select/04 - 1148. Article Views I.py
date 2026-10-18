# Databricks notebook source
# DBTITLE 1,Cell 1
# MAGIC %md
# MAGIC ## 1148. Article Views I (Easy)
# MAGIC
# MAGIC ### Table: `Views`
# MAGIC
# MAGIC | Column Name | Type |
# MAGIC | --- | --- |
# MAGIC | `article_id` | `int` |
# MAGIC | `author_id` | `int` |
# MAGIC | `viewer_id` | `int` |
# MAGIC | `view_date` | `date` |
# MAGIC
# MAGIC * This table does not have a primary key, so it may contain duplicate rows.
# MAGIC * Each row indicates that a viewer viewed an article written by an author on a specific date.
# MAGIC * If `author_id = viewer_id`, it means the author viewed their own article.
# MAGIC
# MAGIC ### Task
# MAGIC Find all authors who viewed at least one of their own articles.
# MAGIC
# MAGIC Return the result table sorted by `id` in ascending order.
# MAGIC
# MAGIC ### Example
# MAGIC
# MAGIC **Input:** `Views`
# MAGIC
# MAGIC | article_id | author_id | viewer_id | view_date |
# MAGIC | --- | --- | --- | --- |
# MAGIC | 1 | 3 | 5 | 2019-08-01 |
# MAGIC | 1 | 3 | 6 | 2019-08-02 |
# MAGIC | 2 | 7 | 7 | 2019-08-01 |
# MAGIC | 2 | 7 | 6 | 2019-08-02 |
# MAGIC | 4 | 7 | 1 | 2019-07-22 |
# MAGIC | 3 | 4 | 4 | 2019-07-21 |
# MAGIC | 3 | 4 | 4 | 2019-07-21 |
# MAGIC
# MAGIC **Output:**
# MAGIC
# MAGIC | id |
# MAGIC | --- |
# MAGIC | 4 |
# MAGIC | 7 |
# MAGIC
# MAGIC **Explanation:**
# MAGIC
# MAGIC * Author `4` viewed at least one of their own articles.
# MAGIC * Author `7` also viewed at least one of their own articles.
# MAGIC * Duplicate rows do not change the final result.

# COMMAND ----------

# DBTITLE 1,Initialisation
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("Leet_Select_4").getOrCreate()

data = [
    [1, 3, 5, "2019-08-01"],
    [1, 3, 6, "2019-08-02"],
    [2, 7, 7, "2019-08-01"],
    [2, 7, 6, "2019-08-02"],
    [4, 7, 1, "2019-07-22"],
    [3, 4, 4, "2019-07-21"],
    [3, 4, 4, "2019-07-21"]
]
columns = ["article_id", "author_id", "viewer_id", "view_date"]

views = spark.createDataFrame(data, columns)

display(views)
views.createOrReplaceTempView("Views")


# COMMAND ----------

# DBTITLE 1,SQL
# MAGIC %sql
# MAGIC SELECT DISTINCT
# MAGIC     author_id AS id
# MAGIC FROM
# MAGIC     Views
# MAGIC WHERE
# MAGIC     author_id = viewer_id
# MAGIC ORDER BY
# MAGIC     1;

# COMMAND ----------

# DBTITLE 1,PySpark
from pyspark.sql.functions import col

result = (views
          .filter(col("author_id") == col("viewer_id"))
          .select(col("author_id").alias("id"))
          .distinct()
          .orderBy("id")
        )

display(result)