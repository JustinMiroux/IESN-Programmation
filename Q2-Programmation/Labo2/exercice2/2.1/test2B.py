import json

f = open("myjson.json", "r", encoding="utf-8")

a_from_json = json.loads(f.read())
print(type(a_from_json))
print(a_from_json)
