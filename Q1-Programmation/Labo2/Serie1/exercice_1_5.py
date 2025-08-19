# -*- coding: utf-8 -*-

""" Labo 2 - Exercice 1.4 """

class MyObject:
    """Just a class"""

    def __init__(self):
        self._protected_var = 1
        self.__private_var = 2


m = MyObject()
print(m._protected_var)
print(m.__private_var)
