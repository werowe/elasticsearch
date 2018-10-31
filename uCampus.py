import csv
import json
import requests
import hashlib

url="http://172.31.46.15:9200/universities/universities/"


f = open('InstitutionCampus.csv') 
    
reader = csv.DictReader(f)

for d in reader:
    j = json.dumps(d)
    m = hashlib.sha1()
    m.update(bytes(j, 'utf-8'))
    id = m.hexdigest()
    response = requests.post(url + id, json=d)
    print (response.json())
