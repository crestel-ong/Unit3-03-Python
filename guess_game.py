#!/usr/bin/env python3

# Created by: Crestel Ong
# Created on: Sept 2021
# This program sees if you can guess the number it generates

import random


def main():
    # this function sees if you can guess the number

    # this is the where the random number is generated from
    computer_number = random.randint(1, 10)

    # input
    guess_number = int(input("Enter a number between 1 - 10: "))

    # process and output
    if guess_number == computer_number:
        print("You guessed correctly!")
    else:
        print("Incorrect, the number was {0}.".format(computer_number))
        print("\nDone.")


if __name__ == "__main__":
    main()
