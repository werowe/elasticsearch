from pyspark import SparkContext, SparkConf
from pyspark.sql import SQLContext
from pyspark.sql.functions import lit

conf = SparkConf().setAppName("updateSchools")
sc = SparkContext(conf=conf)
sc.setLogLevel("INFO")
spark = SQLContext(sc)

reader = spark.read.format("org.elasticsearch.spark.sql").option("es.read.metadata", "true").option("es.nodes.wan.only","true").option("es.port","9200").option("es.net.ssl","false").option("es.nodes", "http://localhost")

df = reader.load("school")
df.show()

df.filter(df["school"] == "Harvard").show()

r=df.rdd.collect()
id = r[0][1]['_id']

df2=df.withColumn("_id", lit(id)) 

esconf={}
esconf["es.mapping.id"] = "_id"
esconf["es.nodes"] = "localhost"
esconf["es.port"] = "9200"
esconf["es.update.script.inline"] = "ctx._source.location = params.location"
esconf["es.update.script.params"] = "location:<Cambridge>"
esconf["es.write.operation"] = "upsert"

df2.write.format("org.elasticsearch.spark.sql").options(**esconf).mode("append").save("school/info")
