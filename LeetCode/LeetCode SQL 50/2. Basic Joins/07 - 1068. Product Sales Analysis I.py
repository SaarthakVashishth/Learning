# Databricks notebook source
# DBTITLE 1,Cell 1
# MAGIC %md
# MAGIC ## 1068. Product Sales Analysis I (Easy)
# MAGIC
# MAGIC ### Table: `Sales`
# MAGIC
# MAGIC | Column Name | Type |
# MAGIC | --- | --- |
# MAGIC | `sale_id` | `int` |
# MAGIC | `product_id` | `int` |
# MAGIC | `year` | `int` |
# MAGIC | `quantity` | `int` |
# MAGIC | `price` | `int` |
# MAGIC
# MAGIC * (`sale_id`, `year`) is the primary key.
# MAGIC * `product_id` is a foreign key referencing `Product`.
# MAGIC * Each row stores a sale for a product in a given year.
# MAGIC * `price` is the per-unit price.
# MAGIC
# MAGIC ### Table: `Product`
# MAGIC
# MAGIC | Column Name | Type |
# MAGIC | --- | --- |
# MAGIC | `product_id` | `int` |
# MAGIC | `product_name` | `varchar` |
# MAGIC
# MAGIC * `product_id` is the primary key.
# MAGIC * Each row stores the name of a product.
# MAGIC
# MAGIC ### Task
# MAGIC Report the `product_name`, `year`, and `price` for each sale in `Sales`.
# MAGIC
# MAGIC Return the result table in any order.
# MAGIC
# MAGIC ### Example
# MAGIC
# MAGIC **Input:** `Sales`
# MAGIC
# MAGIC | sale_id | product_id | year | quantity | price |
# MAGIC | --- | --- | --- | --- | --- |
# MAGIC | 1 | 100 | 2008 | 10 | 5000 |
# MAGIC | 2 | 100 | 2009 | 12 | 5000 |
# MAGIC | 7 | 200 | 2011 | 15 | 9000 |
# MAGIC
# MAGIC **Input:** `Product`
# MAGIC
# MAGIC | product_id | product_name |
# MAGIC | --- | --- |
# MAGIC | 100 | Nokia |
# MAGIC | 200 | Apple |
# MAGIC | 300 | Samsung |
# MAGIC
# MAGIC **Output:**
# MAGIC
# MAGIC | product_name | year | price |
# MAGIC | --- | --- | --- |
# MAGIC | Nokia | 2008 | 5000 |
# MAGIC | Nokia | 2009 | 5000 |
# MAGIC | Apple | 2011 | 9000 |
# MAGIC
# MAGIC **Explanation:**
# MAGIC
# MAGIC * Sale `1` shows that `Nokia` was sold for `5000` in `2008`.
# MAGIC * Sale `2` shows that `Nokia` was sold for `5000` in `2009`.
# MAGIC * Sale `7` shows that `Apple` was sold for `9000` in `2011`.

# COMMAND ----------

# DBTITLE 1,Initialisation
sales_data = [
            [1,100,2008,10,5000], [2,100,2009,12,5000], [7,200,2011,15,9000]
        ]
sales_col = ["sale_id","product_id","year","quantity","price"]

product_data = [
            [100,"Nokia"], [200,"Apple"], [300,"Samsung"]
        ]
product_col = ["product_id","product_name"]

sales = spark.createDataFrame(sales_data, sales_col)
product = spark.createDataFrame(product_data, product_col)

display(sales)
display(product)

sales.createOrReplaceTempView("Sales")
product.createOrReplaceTempView("Product")

# COMMAND ----------

# DBTITLE 1,SQL
# MAGIC %sql
# MAGIC SELECT
# MAGIC     b.product_name
# MAGIC     ,a.year
# MAGIC     ,a.price
# MAGIC FROM
# MAGIC     Sales a
# MAGIC JOIN
# MAGIC     Product b
# MAGIC ON
# MAGIC     a.product_id = b.product_id;

# COMMAND ----------

# DBTITLE 1,PySpark
result = (sales
          .join(product, sales["product_id"] == product["product_id"], "inner")
          .select(product["product_name"], sales["year"], sales["price"])
        )
display(result)