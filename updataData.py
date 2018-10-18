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
