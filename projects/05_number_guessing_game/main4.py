import random
print("Hey! Can you help to guess a number between 1 to 10!")
play_again = False

while not play_again:
    winning_number = random.randint(0, 10)
    counter = 0
    level = input("Choose difficulty, Easy or Hard?: ").lower()
    if level == "easy":
        counter = 10
    elif level == "hard":
        counter = 5
    while counter != 0:
        print(f"you have {counter} attempts left ")
        guessed_number = int(input("Guess a number: "))
        if guessed_number == winning_number:
            print("You won")
            counter = 0
            play_again = input("would you like to play again? Type yes or no!: " )
            if play_again == "yes":
                play_again = False
            else:
                play_again = True
        else:
            if guessed_number < winning_number:
                print("Its too low")
            else:
                print("Its too high")
            counter -= 1
        