import json
import hashlib
import re

def addId(data):
    j=json.dumps(data).encode('ascii', 'ignore')
    data['doc_id'] = hashlib.sha224(j).hexdigest()
    return (data['doc_id'], json.dumps(data))


def parse(str):
    s=p.match(str)
    d = {}
    d['ip']=s.group(1)
    d['date']=s.group(4)
    d['operation']=s.group(5)
    d['uri']=s.group(6)
    return d    

regex='^(\S+) (\S+) (\S+) \[([\w:/]+\s[+\-]\d{4})\] "(\S+)\s?(\S+)?\s?(\S+)?" (\d{3}|-) (\d+|-)\s?"?([^"]*)"?\s?"?([^"]*)?"?$'

p=re.compile(regex)

rdd = sc.textFile("/home/ubuntu/walker/apache_logs")

rdd2 = rdd.map(parse)

rdd3 = rdd2.map(addID)

es_write_conf = {
        "es.nodes" : "localhost",
        "es.port" : "9200",
        "es.resource" : 'walker/apache',
        "es.input.json": "yes",
        "es.mapping.id": "doc_id"
    }
    
    
rdd3.saveAsNewAPIHadoopFile(
        path='-',
     outputFormatClass="org.elasticsearch.hadoop.mr.EsOutputFormat",       keyClass="org.apache.hadoop.io.NullWritable",
        valueClass="org.elasticsearch.hadoop.mr.LinkedMapWritable",
        conf=es_write_conf)
