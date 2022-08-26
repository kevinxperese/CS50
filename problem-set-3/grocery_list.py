"""CS50P -- Problem Set 3: Grocery List
Source: https://cs50.harvard.edu/python/2022/psets/3/grocery/

Suppose that you're in the habit of making a list of items you need from the grocery store.

In a file called grocery.py, implement a program that prompts the user for items, one per line,
until the user inputs control-d (which is a common way of ending one's input to a program).

Then output the user's grocery list in all uppercase, sorted alphabetically by item, prefixing each
line with the number of times the user inputted that item. No need to pluralize the items.

Treat the user's input case-insensitively.
"""

groceries = {}

while True:
    try:
        item = input('Item: ').upper()
        if item in groceries:
            groceries[item] += 1
        else:
            groceries[item] = 1

    except KeyboardInterrupt:
        print('\n')
        break
for item in sorted(groceries.keys()):
    print(f'{groceries[item]} {item}')