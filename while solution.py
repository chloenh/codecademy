#Use a while loop to let the user keep guessing so long as guesses_left is greater than zero.

from random import randint

random_number = randint(1, 10)

guesses_left = 3

while guesses_left > 0:
  guess = int(raw_input("Your guess: "))
  if guess == random_number:
    print "You win!"
    break
  guesses_left -= 1
else:
  print "You lose."
