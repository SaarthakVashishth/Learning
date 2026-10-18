# Databricks notebook source
# /// script
# [tool.databricks.environment]
# environment_version = "6"
# ///
# DBTITLE 1,Cell 1
# MAGIC %md
# MAGIC ## 1280. Students and Examinations (Easy)
# MAGIC
# MAGIC ### Table: `Students`
# MAGIC
# MAGIC | Column Name | Type |
# MAGIC | --- | --- |
# MAGIC | `student_id` | `int` |
# MAGIC | `student_name` | `varchar` |
# MAGIC
# MAGIC * `student_id` is the primary key.
# MAGIC * Each row stores one student's ID and name.
# MAGIC
# MAGIC ### Table: `Subjects`
# MAGIC
# MAGIC | Column Name | Type |
# MAGIC | --- | --- |
# MAGIC | `subject_name` | `varchar` |
# MAGIC
# MAGIC * `subject_name` is the primary key.
# MAGIC * Each row stores one subject name.
# MAGIC
# MAGIC ### Table: `Examinations`
# MAGIC
# MAGIC | Column Name | Type |
# MAGIC | --- | --- |
# MAGIC | `student_id` | `int` |
# MAGIC | `subject_name` | `varchar` |
# MAGIC
# MAGIC * This table has no primary key, so it may contain duplicate rows.
# MAGIC * Each row indicates that a student attended the exam for a subject.
# MAGIC * Every student is expected to take every subject.
# MAGIC
# MAGIC ### Task
# MAGIC Find the number of times each student attended each exam.
# MAGIC
# MAGIC Return the result table ordered by `student_id` and `subject_name`.
# MAGIC
# MAGIC ### Example
# MAGIC
# MAGIC **Input:** `Students`
# MAGIC
# MAGIC | student_id | student_name |
# MAGIC | --- | --- |
# MAGIC | 1 | Alice |
# MAGIC | 2 | Bob |
# MAGIC | 13 | John |
# MAGIC | 6 | Alex |
# MAGIC
# MAGIC **Input:** `Subjects`
# MAGIC
# MAGIC | subject_name |
# MAGIC | --- |
# MAGIC | Math |
# MAGIC | Physics |
# MAGIC | Programming |
# MAGIC
# MAGIC **Input:** `Examinations`
# MAGIC
# MAGIC | student_id | subject_name |
# MAGIC | --- | --- |
# MAGIC | 1 | Math |
# MAGIC | 1 | Physics |
# MAGIC | 1 | Programming |
# MAGIC | 2 | Programming |
# MAGIC | 1 | Physics |
# MAGIC | 1 | Math |
# MAGIC | 13 | Math |
# MAGIC | 13 | Programming |
# MAGIC | 13 | Physics |
# MAGIC | 2 | Math |
# MAGIC | 1 | Math |
# MAGIC
# MAGIC **Output:**
# MAGIC
# MAGIC | student_id | student_name | subject_name | attended_exams |
# MAGIC | --- | --- | --- | --- |
# MAGIC | 1 | Alice | Math | 3 |
# MAGIC | 1 | Alice | Physics | 2 |
# MAGIC | 1 | Alice | Programming | 1 |
# MAGIC | 2 | Bob | Math | 1 |
# MAGIC | 2 | Bob | Physics | 0 |
# MAGIC | 2 | Bob | Programming | 1 |
# MAGIC | 6 | Alex | Math | 0 |
# MAGIC | 6 | Alex | Physics | 0 |
# MAGIC | 6 | Alex | Programming | 0 |
# MAGIC | 13 | John | Math | 1 |
# MAGIC | 13 | John | Physics | 1 |
# MAGIC | 13 | John | Programming | 1 |
# MAGIC
# MAGIC **Explanation:**
# MAGIC
# MAGIC * The result must include every student-subject combination.
# MAGIC * `Alice` attended `Math` 3 times, `Physics` 2 times, and `Programming` 1 time.
# MAGIC * `Bob` attended `Math` once, `Programming` once, and did not attend `Physics`.
# MAGIC * `Alex` did not attend any exams.
# MAGIC * `John` attended each subject exactly once.

# COMMAND ----------

# DBTITLE 1,Initialization
students_data = [
    (1, "Alice"),
    (2, "Bob"),
    (13, "John"),
    (6, "Alex"),
]
students = spark.createDataFrame(students_data, ["student_id", "student_name"])

subjects_data = [
    ("Math",),
    ("Physics",),
    ("Programming",),
]
subjects = spark.createDataFrame(subjects_data, ["subject_name"])

examinations_data = [
    (1, "Math"),
    (1, "Physics"),
    (1, "Programming"),
    (2, "Programming"),
    (1, "Physics"),
    (1, "Math"),
    (13, "Math"),
    (13, "Programming"),
    (13, "Physics"),
    (2, "Math"),
    (1, "Math"),
]
examinations = spark.createDataFrame(examinations_data, ["student_id", "subject_name"])

students.createTempView("Students")
subjects.createTempView("Subjects")
examinations.createTempView("Examinations")

# COMMAND ----------

# DBTITLE 1,SQL
# MAGIC %sql
# MAGIC SELECT
# MAGIC     a.student_id
# MAGIC     , a.student_name
# MAGIC     , a.subject_name
# MAGIC     , SUM(
# MAGIC         CASE 
# MAGIC             WHEN b.student_id IS NULL THEN 0
# MAGIC             ELSE 1
# MAGIC         END) AS attended_exams
# MAGIC FROM
# MAGIC     (Students CROSS JOIN Subjects) AS a
# MAGIC LEFT JOIN
# MAGIC     Examinations AS b
# MAGIC ON
# MAGIC     a.student_id = b.student_id
# MAGIC AND
# MAGIC     a.subject_name = b.subject_name
# MAGIC GROUP BY
# MAGIC     a.student_id
# MAGIC     , a.student_name
# MAGIC     , a.subject_name
# MAGIC ORDER BY
# MAGIC     a.student_id
# MAGIC     , a.subject_name;

# COMMAND ----------

# DBTITLE 1,PySpark
result = (
)