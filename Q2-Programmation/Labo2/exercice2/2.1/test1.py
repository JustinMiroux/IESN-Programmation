import json

a = [1, "2", 3, "4"]
print(type(a))

a_json = json.dumps(a)
print(a_json)
print(type(a_json))
print("_________________________________________________________")


b = (1, 2)
print(type(b))

b_json = json.dumps(b)
print(b_json)
print(type(b_json))
print("_________________________________________________________")


c = {"brand": "Renault", "model": "Laguna", "year": 2001}
print(type(c))

c_json = json.dumps(c)
print(c_json)
print(type(c_json))
print("_________________________________________________________")


d = 69
print(type(d))

d_json = json.dumps(d)
print(d_json)
print(type(d_json))
print("_________________________________________________________")


e = 69.420
print(type(e))

e_json = json.dumps(e)
print(e_json)
print(type(e_json))
print("_________________________________________________________")


f = "fuck"
print(type(f))

f_json = json.dumps(f)
print(f_json)
print(type(f_json))
print("_________________________________________________________")


g = True
print(type(g))

g_json = json.dumps(g)
print(g_json)
print(type(g_json))
print("_________________________________________________________")
