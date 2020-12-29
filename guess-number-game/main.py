from art import logo
from replit import clear
import random

game_over = False
while not game_over:
  print(logo)
  print("Welcome to the number guessing game: GuessIT!\n")
  print("I'm thinking a number between 1 and 100.\n")
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")

  if level == 'hard':
    life_number = 5
  else: 
    life_number = 10

  random_number = random.randint(1, 100)
  still_alive = True
  
  while life_number > 0 and still_alive:
      print(f"You have {life_number} remaining to guess the number.\n")
      guess = int(input("Make a guess: "))
      life_number -= 1
      if guess > random_number:
        print("Too high. ")
      elif guess < random_number:
        print("Too low.")
      if guess == random_number:
        print("Nice job! You Ace it! 😎")
        still_alive = False
        game_over = True
  
  if life_number == 0:
    print("You run out all the opportunities and failed 😔.")
    still_alive = False
    game_over = True
  while game_over:
    if input("Want to try again? Type 'y' or 'n': ") == 'y':
      clear()
      still_alive = True
      game_over = False