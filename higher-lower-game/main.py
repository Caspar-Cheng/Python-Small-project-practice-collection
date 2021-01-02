from art import logo, vs 
from game_data import data 
import random 
from replit import clear

def start():
  clear()
  print(logo)

start()
game_over = False
score = 0
while not game_over:
  chosen_list = random.sample(data, 2)
  first = chosen_list[0]
  second = chosen_list[1]
  
  print(f"Compare A: {first['description']}\n")
  print(vs)
  print(f"Against B: {second['description']}\n")
  choice = input("Who has more followers? Type 'A' or 'B': ")
  
  if choice == 'A' and first['follower_count'] > second['follower_count']:
    score += 1
    start()
    print(f"You're right! Current score: {score}")
  elif choice == 'B' and first['follower_count'] < second['follower_count']:
    score += 1
    start()
    print(f"You're right! Current score: {score}")
  else:
    start()
    print(F"Sorry, that's wrong. Final score: {score}")
    game_over = True
    if input("Want to play again? Type 'Y' or 'N': ") == 'Y':
      game_over = False
      start()
      score = 0
