# -*- coding: utf-8 -*-
"""Guessing_number_game

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1meMhTTsecUTEuM-5U4Lw1QV2YQROPVg6
"""

import random

topRange = int(input("Enter a top range for the number = "))
number = random.randint(1 , topRange + 1)

running = True
while running:
  guess = int(input("Guess the number: "))

  if guess == number:
    print("You guessed the number")
    running = False
  elif guess > number:
    print("The number is higher")
  else:
    print("The number is lower")





