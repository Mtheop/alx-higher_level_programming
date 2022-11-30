#!/usr/bin/python3
"""Print the numbers from 1 to 100 seperated by a space.
  For multiples of three, print fizz instead of the number
  For multiples of five, print buzz instead of the number.
  For multiples of three and five, print Fizzbuzz instead of the number
 of the number.
    """


def fizbuzz():
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz ", end="")
        elif number % 3 == 0:
            print("Fizz ", end="")
        elif number % 5 == 0:
            print("Buzz ", end="")
        else:
            print("{} ".format(number), end="")
