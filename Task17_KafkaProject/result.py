from pyspark import SparkConf, SparkContext, sql
from pyspark.sql import SparkSession
import mysql.connector
from pyspark.sql.types import ArrayType, StructField, StructType, StringType, IntegerType
import matplotlib.pyplot as plt
import pandas

class Result:

    def Db(self):
        spark = SparkSession.builder.appName(name="Test").master("local[*]").getOrCreate()
        sc = spark.sparkContext
        sc.setLogLevel("ERROR")
        mydb = mysql.connector.connect(host="localhost", user="root", password="password", database="news")
        mycursor = mydb.cursor()
        mycursor.execute("SELECT section,title,abstract,byline,item_type,source,material_type_facet,counter from news_detail")
        myresult = mycursor.fetchall()

        schema = StructType([
            StructField('section', StringType(), True),
            StructField('title', StringType(), True),
            StructField('abstract', StringType(), True),
            StructField('byline', StringType(), True),
            StructField('item_type', StringType(), True),
            StructField('source', StringType(), True),
            StructField('material_type_facet', StringType(), True),
            StructField('counter', IntegerType(), True)
        ])
        # # Convert list to RDD
        rdd = spark.sparkContext.parallelize(myresult)
        # # Create data frame
        df = spark.createDataFrame(rdd, schema)
        return df

    def myReports(self):
        df = self.Db()
        dfplot = df.groupby("section").sum("counter").sort("section")
        #print(dfplot.show())
        return dfplot

        # x = dfplot.toPandas()["section"].values.tolist()
        # y = dfplot.toPandas()["sum(counter)"].values.tolist()
        # plt.bar(x, y)
        # plt.show()


obj = Result()
obj.myReports()
