import requests
import random
import hashlib
import json

url="http://parisx:9200/universities/universities/" 

def assignClasses():
    classes=[]
    for x in range(random.randrange(1,6)):
      classes.append(genclass())
    return classes 
      
schools = ("Arizona State University", "University of South Carolina - Columbia", "University of North Carolina at Chapel Hill") 
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
    students["school"]=schools[random.randrange(0,3)]
    students["firstName"] = firstNames[random.randrange(0,3)]
    students["lastName"] = lastNames[random.randrange(0,3)]
    students["classes"] = assignClasses()

    m = hashlib.sha1()
    m.update(bytes(json.dumps(students), 'utf-8'))
    id = m.hexdigest()

    response = requests.post(url + id, json=students)


for r in range(1,40000):
    genStudent()
