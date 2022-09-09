"""CS50P -- Problem Set 3: Felipe's Taqueria
Source: https://cs50.harvard.edu/python/2022/psets/3/taquaria/
One of the most popular places to eat in Harvard Square is Felipe's Taqueria, which offers a menu of
entrees, per the dict below, wherein the value of each key is a price in dollars:

{
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

In a file called taqueria.py, implement a program that enables a user to place an order, prompting
them for items, one per line, until the user inputs control-d (which is a common way of ending one's
input to a program).

After each inputted item, display the total cost of all items inputted thus far, prefixed with a
dollar sign ($) and formatted to two decimal places. Treat the user's input case insensitively.
Ignore any input that isn't an item. Assume that every item on the menu will be titlecased.
"""

menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

running_total = 0

while True:
    try:
        item = input('Item: ').title()
        running_total += menu[item]
        print(f'Total: ${running_total:.2f}')

    except KeyError:
        print('KeyError caught')
        pass

    except EOFError:  # ctrl+z on Windows, ctrl+d on Linux/Mac
        print('EOFError caught')
        break

    except KeyboardInterrupt:  # ctrl+c on Windows and Mac/Linux
        print('KeyboardInterrupt caught')
        break

