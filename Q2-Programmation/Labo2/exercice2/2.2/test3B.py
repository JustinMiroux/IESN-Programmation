import pickle

class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

f = open("dogs.bin", "rb")
dogs_from_bytes = pickle.loads(f.read())

print(type(dogs_from_bytes))
print(dogs_from_bytes.name)
