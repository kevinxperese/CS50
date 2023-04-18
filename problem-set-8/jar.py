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
        return "🍪" * self.num_cookies

    def deposit(self, n):
        if self.num_cookies + n > self._capacity:
            raise ValueError("Oh no! Too many cookies in the cookie jar!")
        else:
            self.num_cookies += n

        return self

    def withdraw(self, n):
        if self.num_cookies - n < 0:
            raise ValueError("You ate all the cookies!")
        else:
            self.num_cookies += -n

        return self

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self.num_cookies


def main():
    jar = Jar()
    jar.deposit(2)
    print(jar)

if __name__ == "__main__":
    main()