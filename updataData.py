from pyspark import SparkContext, SparkConf
from pyspark.sql import SQLContext

reader =spark.read.format("org.elasticsearch.spark.sql").option("es.read.metadata", "true").option("es.nodes.wan.only","true").option("es.port","9200").option("es.net.ssl","false").option("es.nodes", "http://localhost")

df = reader.load("schools")

df.filter(df["school"] == "Harvard").show()

esconf={}
esconf["es.mapping.id" = 1 ]
esconf["es.nodes"] = "localhost"
esconf["es.port"] = "9200"
esconf["es.update.script.inline"] = "ctx._source.location = params.location"
esconf["es.update.script.params"] = "location:<Cambridge>"
esconf["es.write.operation"] = "update"

df.write.format("org.elasticsearch.spark.sql").options(**esconf).mode("overwrite").save("backup_/items")

