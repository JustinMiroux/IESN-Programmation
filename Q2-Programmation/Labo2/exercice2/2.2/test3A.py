import pickle

class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

dog = Dog("faline", 24, 0)
dog_in_bytes = pickle.dumps(dog)

f = open("dogs.bin", "wb")
f.write(dog_in_bytes)
f.close()
