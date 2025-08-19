# -*- coding: utf-8 -*-

""" Labo 2 - Exercice 1.2 """

class MyObject:
    """
    MyObject :
    A class of object
    """

    def say_hello(self):
        """ Says Hello """
        print("Hello!")
        #self.say_hello()

    def add(self, a, b):
        """ Print result of a+b """
        print(a+b)


m = MyObject()
m.say_hello()
m.add(1,2)
