import random
import sys

a,b = [int(sys.argv[1]), int(sys.argv[2])]
number = random.randint(a,b)

guess = int(input(f"Guess a number between {a} and {b}. "))
diff = abs(guess - number)
tries = 1
#possible exceptions: none number input, wrong input param length, non integer argvs
while diff != 0:
  guess = int(input(f"Wrong! Guess a number between {a} and {b}. "))
  tries += 1
  if (abs(guess - number) < diff):
    print("Getting warmer!")
  else:
    print("Getting colder.")
  diff = abs(guess - number)
else:
  print(f"Good job! It took you {tries} tries")
