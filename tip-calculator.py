bill = int(input("How much of the total bill? "))
tip = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
people = int(input("How many people to split the bill? "))

pay = round((bill*(1+tip/100))/people, 2)

print(f"Each person should pay: ${pay}")