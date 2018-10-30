import requests
import random
import hashlib
import json

url="http://172.31.46.15:9200/students/students/" 

def assignClasses():
    classes=[]
    for x in range(random.randrange(1,6)):
      classes.append(genclass())
    return classes 
      

firstNames = ("Walker", "Stephen", "Julie", "George")
lastNames = ("Rowe", "Shakespeare", "Mann", "Sarte")
courses= ("math", "physics", "French", "logic")

def genclass():
    classes={}
    classes["name"]=courses[random.randrange(0,3)]
    classes["grades"] = random.randrange(1,7)
    return classes


def genStudent():
    students={}
    students["firstName"] = firstNames[random.randrange(0,3)]
    students["lastName"] = lastNames[random.randrange(0,3)]
    students["classes"] = assignClasses()

    m = hashlib.sha1()
    m.update(bytes(json.dumps(students), 'utf-8'))
    id = m.hexdigest()
    print(students)
    response = requests.post(url + id, json=students)
    print(response.text)

for r in range(1,4):
    genStudent()
