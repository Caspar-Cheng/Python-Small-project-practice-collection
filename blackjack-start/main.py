from replit import clear
from art import logo
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def calculate(cards):
  if sum(cards) == 21 and len(cards) == 2:
    return 0
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)


def Start():
  player_card = random.choices(cards, k=2)
  computer_card = random.choices(cards, k=2)

  player_number = calculate(player_card)
  computer_number = calculate(computer_card)

  while computer_number != 0 and computer_number < 17:
    computer_card.append(random.choice(cards))
    computer_number = calculate(computer_card)

  print(f"You cards: {player_card}, current score: {player_number}\n")
  print(f"Computer's first card: {computer_card[0]}\n")

  if player_number > 21 or computer_number >21:
    print(compare(player_number, computer_number))
    to_start()

  game_over = False
  while not game_over:
    next_step = input("Type 'y' to get another card, type 'n' to pass: ")

    if next_step == "y":
      new_card = random.choice(cards)
      player_card.append(new_card)

    player_number = calculate(player_card)
    print(f"Your cards: {player_card}, current score: {player_number}")
    print(f"Computer's first card: {computer_card[0]}\n")

    if player_number > 21 or computer_number >21 or next_step == "n":
      game_over = True
      print(f"Your final cards: {player_card}, current score: {player_number}")
      print(f"Computer's final cards: {computer_card}, current score: {computer_number}")
      print(compare(player_number, computer_number))
      to_start()


def compare(num1, num2):
  if num1 > 21 and num2 > 21:
    return "You went over, you lose 😓..."

  if num1 == num2:
    return "Draw 😑"
  elif num1 == 0:
    return "You win with a Blackjack 😎"
  elif num2 == 0:
    return "You lose, opponent has a Blackjack 😱"
  elif num1 > 21:
    return "You went over, you lose 😓..."
  elif num2 > 21:
    return "You win, opponent went over 🤓"
  elif num1 > num2:
    return "You win 😁"
  else: 
    return "You lose 😩"

def to_start():
  if input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
    clear()
    print(logo)
    Start()

to_start()


