"""Problem Set 8: Cookie Jar
Source: https://cs50.harvard.edu/python/2022/psets/8/jar/

"""

class Jar:
    def __init__(self, capacity=12):
        self._capacity = capacity
        self.num_cookies = 0

        if self._capacity < 0:
            raise ValueError("Worst cookie jar ever. Try again.")

    def __str__(self):
        print("🍪" * self.num_cookies)

    def deposit(self, n):
        self.num_cookies += n

        if self.num_cookies > self._capacity:
            raise ValueError("Oh no! Too many cookies in the cookie jar!")

    def withdraw(self, n):
        self.num_cookies -= n

        if self.num_cookies < 0:
            raise ValueError("You ate all the cookies!")

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self.num_cookies

