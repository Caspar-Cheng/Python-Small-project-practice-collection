rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
choices = [rock, paper, scissors]
play_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors\n"))
computer_choice = random.randint(0,2)
print(f"You chose:\n {choices[play_choice]}")
print(f"Computer chose:\n {choices[computer_choice]}")

if play_choice == 0:
  if computer_choice == 1:
    print("You lose...")
  elif computer_choice == 2:
    print("You win!")
  else: 
    print("No winner this round.")
elif play_choice == 1:
  if computer_choice == 2:
    print("You lose...")
  elif computer_choice == 0:
    print("You win!")
  else: 
    print("No winner this round.")
elif play_choice == 2:
  if computer_choice == 0:
    print("You lose...")
  elif computer_choice == 1:
    print("You win!")
  else: 
    print("No winner this round.")