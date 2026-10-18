# Databricks notebook source
# DBTITLE 1,Cell 1
# MAGIC %md
# MAGIC ## 1683. Invalid Tweets (Easy)
# MAGIC
# MAGIC ### Table: `Tweets`
# MAGIC
# MAGIC | Column Name | Type |
# MAGIC | --- | --- |
# MAGIC | `tweet_id` | `int` |
# MAGIC | `content` | `varchar` |
# MAGIC
# MAGIC * `tweet_id` is the primary key (unique values) for this table.
# MAGIC * `content` consists of alphanumeric characters, `'!'`, or spaces.
# MAGIC * This table contains all tweets in a social media app.
# MAGIC
# MAGIC ### Task
# MAGIC Find the IDs of the invalid tweets.
# MAGIC
# MAGIC A tweet is invalid if the number of characters in `content` is strictly greater than `15`.
# MAGIC
# MAGIC Return the result table in any order.
# MAGIC
# MAGIC ### Example
# MAGIC
# MAGIC **Input:** `Tweets`
# MAGIC
# MAGIC | tweet_id | content |
# MAGIC | --- | --- |
# MAGIC | 1 | Let us Code |
# MAGIC | 2 | More than fifteen chars are here! |
# MAGIC
# MAGIC **Output:**
# MAGIC
# MAGIC | tweet_id |
# MAGIC | --- |
# MAGIC | 2 |
# MAGIC
# MAGIC **Explanation:**
# MAGIC
# MAGIC * Tweet `1` has length `11`, so it is valid.
# MAGIC * Tweet `2` has length `33`, so it is invalid.

# COMMAND ----------

from pyspark.sql import SparkSession, Row
spark = SparkSession.builder.appName("Leet_Select_5").getOrCreate()

# creating df from Row method
data = [
        Row(tweet_id=1, content="Let us Code")
        ,Row(tweet_id=2, content="More than fifteen chars are here!")
    ]
tweets = spark.createDataFrame(data)

display(tweets)
tweets.createOrReplaceTempView("Tweets")

# COMMAND ----------

# DBTITLE 1,SQL
# MAGIC %sql
# MAGIC SELECT
# MAGIC     tweet_id
# MAGIC FROM
# MAGIC     Tweets
# MAGIC WHERE
# MAGIC     length(content) > 15;

# COMMAND ----------

# DBTITLE 1,PySpark
from pyspark.sql.functions import col, length
result = (tweets
          .filter(length(col("content")) > 15)
          .select("tweet_id")
        )

display(result)