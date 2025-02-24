import json

a = [1, 'abc', {'x': (5, 8), 'y': "Pas"}]

a_json = json.dumps(a)

f = open("myjson.json", "w", encoding="utf-8")
f.write(a_json)
f.close()
