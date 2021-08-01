import json


keywords = '{ "萬海": 3, "長榮": 1 }'  #  json string

obj = json.loads(keywords)
print(obj)
print(type(obj)) # <class 'dict'>
