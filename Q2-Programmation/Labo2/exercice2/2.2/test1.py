import pickle

a = [1, "2", 3, "4"]
a_bytes = pickle.dumps(a)
print(type(a_bytes))
print(a_bytes)
