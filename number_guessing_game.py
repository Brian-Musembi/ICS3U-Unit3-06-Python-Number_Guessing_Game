#!/usr/bin/env python3

# Created by: Brian Musembi
# Created on: 07 May 2021
# This program allows the user to guess the correct number

import random


def main():
    # this function allows the user to guess the correct number

    # random number generator
    random_number = random.randint(0, 9)

    # input
    user_guess = input("Enter a number between 0 - 9: ")
    print("")

    # process & output
    try:
        user_guess_int = int(user_guess)

        if user_guess_int == random_number:
            print("You guessed right! the number was {}."
                  .format(random_number))

        else:
            print("Incorrect, the number was {}."
                  .format(random_number))

    except Exception:
        print('{} is not a number! Try again.'.format(user_guess))

    finally:
        print("")
        print("Thanks for playing!")


if __name__ == "__main__":
    main()
