import random
import sys

a,b = [int(sys.argv[1]), int(sys.argv[2])]
number = random.randint(a,b)

guess = int(input(f"Guess a number between {a} and {b}. "))
print("To quit game, guess -1 when prompted")
diff = abs(guess - number)
tries = 1
#possible exceptions: none number input, wrong input param length, non integer argvs
start = a
stop = b
count = 1
g = (stop - start) // 2

#A little competition with some binary search action
while g != number:
  c1 = g - 1
  c2 = g + 1
  if abs(number - c1) < abs(number - c2):
    if number - c1 == 0:
      count+=1
      break
    stop = c1
  else:
    if number - c2 == 0:
      count+=1
      break
    start = c2
  g = stop - (stop - start) // 2
  count+=1
  
#Your guess loop
while diff != 0 and guess != -1:
  guess = int(input(f"Wrong! Guess a number between {a} and {b}. "))
  tries += 1
  if (abs(guess - number) < diff):
    print("Getting warmer!")
  else:
    print("Getting colder.")
  diff = abs(guess - number)

if guess == -1:
  print(f"You gave up at try number {tries}! Binary Search: {count}")
elif tries < count:
  print(f"Good job, you beat binary search! You: {tries}, Binary Search: {count} ")
else:
  print(f"Aw, maybe next time! You: {tries}, Binary Searh {count}")
