"""CS50P -- Problem Set 4: Guessing Game
Source: https://cs50.harvard.edu/python/2022/psets/4/game/

I'm thinking of a number between 1 and 100…

What is it?
In a file called game.py, implement a program that:

Prompts the user for a level, . If the user does not input a positive integer, the program should prompt again.
Randomly generates an integer between 1 and , inclusive, using the random module.
Prompts the user to guess that integer. If the guess is not a positive integer, the program should prompt the user again.
If the guess is smaller than that integer, the program should output Too small! and prompt the user again.
If the guess is larger than that integer, the program should output Too large! and prompt the user again.
If the guess is the same as that integer, the program should output Just right! and exit.
"""

import random

# Ask user for a level
while True:
    level = int(input('Choose a level:\n'))
    if level > 0:
        break

# Choose a random number between 1 and level
my_number = random.choice(range(1, level+1))

print(f"Cool. I'm thinking of a number between 1 and {level}. Have a guess!")

# Ask user to guess my_number.
while True:
    guess = int(input())
    if guess > level:
        print('Silly Goose. You chose a number greater than level! Try again.')
    if guess < my_number:
        print('Too small! Try again:')
        continue
    elif guess > my_number:
        print('Too large! Try again:')
        continue
    elif guess == my_number:
        print('Just right! Well done.')
        break
