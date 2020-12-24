from replit import clear
from art import logo

print(logo)
bid_collection =  {}
bid_finished = False

def find_highest_bid (bid_record):
  highest = 0
  winner = ""
  for bidder in bid_record:
    bid_amount = bid_record[bidder]
    if bid_amount > highest:
      highest = bid_amount
      winner = bidder
  print(f"The winner is {winner} with bid price on {highest}!")

while not bid_finished:
  name = input("What's your name? ")
  price = int(input("What's your bid price? "))
  bid_collection[name] = price

  to_continue = input("If there are other person who want to bid? 'yes' or 'no'? \n")
  if to_continue == 'no':
    bid_finished = True
    find_highest_bid(bid_collection)
  elif to_continue == 'yes':
    clear()



