"""CS50P -- Problem Set 6: Pizza Py
Source: https://cs50.harvard.edu/python/2022/psets/6/pizza/

Do not use `tabulate` package -- we don't have it installed.

"""

import pandas as pd

pizza_menu = pd.read_csv('https://cs50.harvard.edu/python/2022/psets/6/pizza/regular.csv')
print(pizza_menu.to_string(index=False))