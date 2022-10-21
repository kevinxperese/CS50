"""CS50P -- Problem Set 4: Little Professor
Source: https://cs50.harvard.edu/python/2022/psets/4/professor/

One of David's first toys as a child, funny enough, was Little Professor, a “calculator” that would
generate ten different math problems for David to solve.

For instance, if the toy were to display 4 + 0 = , David would (hopefully) answer with 4.
If the toy were to display 4 + 1 = , David would (hopefully) answer with 5.
If David were to answer incorrectly, the toy would display EEE.
And after three incorrect answers for the same problem, the toy would simply display the correct answer (e.g., 4 + 0 = 4 or 4 + 1 = 5).

In a file called professor.py, implement a program that:

Prompts the user for a level, . If the user does not input 1, 2, or 3, the program should prompt again.

Randomly generates ten (10) math problems formatted as X + Y = , wherein each of X and Y is a non-negative integer with level digits.
No need to support operations other than addition (+).

Prompts the user to solve each of those problem.
If an answer is not correct (or not even a number), the program should output EEE and prompt the user again,
allowing the user up to three tries in total.
If the user has still not answered correctly after three tries, the program should output the correct answer.

The program should ultimately output the user's score, a number out of 10.
Structure your program as follows, wherein get_level prompts (and, if need be, re-prompts)
the user for a level and returns 1, 2, or 3, and generate_integer returns a randomly generated
non-negative integer with level digits or raises a ValueError if level is not 1, 2, or 3:
"""

import random


def main():
    print("Let's play a game.")
    print("First, choose a level:")
    level = get_level()

    NUM_MATH_PROBLEMS = 10
    print(f"Cool. I'll now ask you {NUM_MATH_PROBLEMS} math problems. Let's see how you do!")

    score = 0

    for prob_num in range(NUM_MATH_PROBLEMS):
        x = generate_integer(level)
        y = generate_integer(level)

        try_num = 0
        while try_num < 3:
            try:
                answer = int(input(f"Problem {prob_num+1}: What's {x} + {y}? "))
            except:
                print('You need to enter an integer. Try again, please!')

            if answer == x + y:
                score += 1
                print('Nice!')
                break
            else:
                print('EEE!')
                try_num += 1
                print(f'Try again (you have {3-try_num} tries left.)')
                continue

        if try_num == 3:
            print(f'Sorry. The correct answer is {x + y}. On to problem {prob_num+2}!')

    print(f"You're total score was: {score} / {NUM_MATH_PROBLEMS}")


def get_level():
    while True:
        try:
            level = int(input('Enter a level between 1 and 3: '))
            if level in [1, 2, 3]:
                return level
            else:
                print('You need to enter an integer betwen 1 and 3. Please try again.')
        except:
            print('You need to enter an integer betwen 1 and 3. Please try again.')


def generate_integer(level):
    if level not in [1, 2, 3]:
        raise ValueError
    else:
        return random.choice(range(1, 10 ** level))


if __name__ == "__main__":
    main()
