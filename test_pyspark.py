from pyspark.sql import SparkSession
from pyspark import SparkConf
import configparser

def get_spark_app_config():
    spark_conf = SparkConf()
    config = configparser.ConfigParser()
    config.read("./conf/spark.conf")
    
    for key in config["SPARK_APP_CONF"]:
        spark_conf.set(key, config["SPARK_APP_CONF"][key])
    
    return spark_conf

if __name__ == "__main__":
    conf = get_spark_app_config()
    spark = SparkSession.builder \
        .config(conf=conf) \
        .getOrCreate()

    df = spark.createDataFrame([("Ravi", 28), ("Suraj", 24)], ["Name", "Age"])
    df.show()

    spark.stop()
