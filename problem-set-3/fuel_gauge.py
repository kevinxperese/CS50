"""CS50P -- Problem Set 3: Fuel Gauge
Source: https://cs50.harvard.edu/python/2022/psets/3/fuel/

Fuel gauges indicate, often with fractions, just how much fuel is in a tank. For instance 1/4
indicates that a tank is 25% full, 1/2 indicates that a tank is 50% full, and 3/4 indicates that a
tank is 75% full.

In a file called fuel.py, implement a program that prompts the user for a fraction, formatted as X/Y,
wherein each of X and Y is an integer, and then outputs, as a percentage rounded to the nearest
integer, how much fuel is in the tank. If, though, 1% or less remains, output E instead to indicate
that the tank is essentially empty. And if 99% or more remains, output F instead to indicate that
the tank is essentially full.

If, though, X or Y is not an integer, X is greater than Y, or Y is 0, instead prompt the user again.
(It is not necessary for Y to be 4.)

Be sure to catch any exceptions like ValueError or ZeroDivisionError.
"""

def get_fraction() -> tuple:
    numerator, denominator = input('Fraction: ').split('/')
    return (int(numerator), int(denominator))


def calc_fuel_level(numerator: int, denominator: int) -> str:
    if numerator / denominator >= 0.99:
        return 'F'
    elif numerator / denominator <= 0.01:
        return 'E'
    else:
        return f'{round((numerator / denominator) * 100)}%'


good_response = False
while good_response == False:
    try:
        numerator, denominator = get_fraction()
        print(calc_fuel_level(numerator, denominator))
        good_response = True
    except ValueError:
        # print('ValueError caught')
        pass
    except ZeroDivisionError:
        # print('ZeroDivisionError caught')
        pass