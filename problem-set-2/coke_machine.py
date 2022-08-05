"""CS50P -- Problem Set 2: Coke Machine
Source: https://cs50.harvard.edu/python/2022/psets/2/coke/

Suppose that a machine sells bottles of Coca-Cola (Coke) for 50 cents and only accepts coins in
these denominations: 25 cents, 10 cents, and 5 cents.

In a file called coke.py, implement a program that prompts the user to insert a coin, one at a time,
each time informing the user of the amount due.

Once the user has inputted at least 50 cents, output how many cents in change the user is owed.
Assume that the user will only input integers, and ignore any integer that isn't an accepted
denomination.
"""

amount_due = 50

while amount_due > 0:
    coin = input('Insert coin: ')

    if coin in ['25', '10', '5']:
        amount_due -= int(coin)
        print(f'Amount due: {amount_due}')
    else:
        # Restate the amount due if coin isn't an acceptable denomination
        print(f'Amount due: {amount_due}')

    if amount_due < 0:
        change_owed = amount_due * -1
        print(f'Change owed: {change_owed}')
