#!/usr/bin/python3
def fizzbuzz():
    """prints from 1 to 100 separated by a space
    prints Fizz for multiples of three
    prints Buzz for multiples of five
    prints FizzBuzz for multiples of both three and five
    """
    for num in range(1, 100):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz", end="")
        elif num % 3 == 0:
            print("Fizz", end="")
        elif num % 5 == 0:
            print("Buzz", end="")
        else:
            print("{}".format(num), end="")
