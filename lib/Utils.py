from pyspark.sql import SparkSession


def get_spark_session(env):
    if env == "LOCAL":
        return SparkSession.builder \
            .config('spark.driver.extraJavaOptions',
                    '-Dlog4j.configurationFile=file:log4j2.properties') \
            .master("local[2]") \
            .enableHiveSupport() \
            .getOrCreate()
    else:
        return SparkSession.builder \
            .enableHiveSupport() \
            .getOrCreate()
