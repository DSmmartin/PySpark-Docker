""" This is an example of an PySpark app """

import sys
from pyspark.sql import SparkSession


print('I started PySpark')
spark = SparkSession.builder.appName('dev').getOrCreate()
print("Spark configuration")
print(spark.sparkContext.uiWebUrl)
print(spark.sparkContext.getConf().getAll())
print('****************')
print('Python version: {}'.format(sys.version))
print('Spark version: {}'.format(spark.version))

spark.stop()