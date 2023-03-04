"""Problem Set 8: Cookie Jar
Source: https://cs50.harvard.edu/python/2022/psets/8/jar/

"""

class Jar:
    def __init__(self, capacity=12):
        ...

    def __str__(self):
        ...

    def deposit(self, n):
        ...

    def withdraw(self, n):
        ...

    @property
    def capacity(self):
        ...

    @property
    def size(self):
        ...