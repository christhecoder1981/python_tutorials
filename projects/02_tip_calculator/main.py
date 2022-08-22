print("Welcome to the tip calculator!")
total = int(input("Whats the total bill? "))
tip = int(input("How much tip would you like to give, 10, 12, 15 ? "))
guests = int(input("How many people to split the bill? "))
tip_p = tip / 100 * total
tot = total + tip_p
price_p = tot / guests
print(f"Each person should pay {price_p}")
