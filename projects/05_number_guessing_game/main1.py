winning_number = 5

print("Hey! Can you help to guess a number between 1 to 10!")

number = int(input("Guess the number: "))
if number < winning_number:
    print("Number is to low")
elif number > winning_number:
    print("Number is too high")
elif number == winning_number:
    print("Congrats you won! ")