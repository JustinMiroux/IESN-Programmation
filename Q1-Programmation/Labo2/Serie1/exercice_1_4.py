# -*- coding: utf-8 -*-

""" Labo 2 - Exercice 1.4 """

class MyObject:
    """
    Variable de classe (int)
    """

    class_var = 1


class MySecondObject:
    """
    Varible de classe (list vide)
    """

    class_var = []


a1 = MyObject.class_var
b1 = MyObject.class_var = 2

print(bool(a1 == b1))
print(bool(a1 is b1))

a2 = MySecondObject.class_var
b2 = MySecondObject.class_var # I don't know how !
