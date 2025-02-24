import pickle

a = [1, 'abc', {'x': (5, 8), 'y': "Pas"}]
a_bytes = pickle.dumps(a)
print(a_bytes)
print(type(a_bytes))

a_from_bytes = pickle.loads(a_bytes)
print(a_from_bytes)
print(type(a_from_bytes))
