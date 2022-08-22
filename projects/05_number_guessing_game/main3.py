import random
winning_number = random.randint(0, 10)

print("Hey! Can you help to guess a number between 1 to 10!")

is_game_over = False

while not is_game_over:
    guessed_number = int(input("Guess a number: "))
    if guessed_number == winning_number:
        print("Congrats! You Won!")
        is_game_over = True
    else:
        if guessed_number < winning_number:
            print("It's Low")
        else:
            print("It's High")