# -*- coding: utf-8 -*-

""" Labo 2 - Exercice 1.3 """

class Animal:
    """
    Animal
    has 2 propreties (weight an species)
    """

    def __init__(self, weight, species):
        self.weight = weight
        self.species = species

    def print_info(self):
        """ Print the weight and species """
        print(f"Weight : {self.weight}")
        print(f"Species : {self.species}")


cat = Animal("5Kg", "Feline")
dog = Animal("10Kg", "Canine")

cat.print_info()
dog.print_info()

print(cat.__class__)
