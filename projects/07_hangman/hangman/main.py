# Importing Dependencies!
import random
from hangman_art import stages, logo
from hangman_words import word_list

# Printing Logo!
print(logo)

# Creating Global Variables
game_is_finished = False
lives = len(stages) - 1

chosen_word = random.choice(word_list) # chris
word_length = len(chosen_word) # 5

print(chosen_word)

display = []
for i in range(word_length):
    display.append("_")

while not game_is_finished:
    guess = input("Guess a letter: ") # r

    if guess in display:
        print(f"You have already guessed {guess}")

    for pos in range(word_length):
        letter = chosen_word[pos]
        if letter == guess:
            display[pos] = letter
    
    print(f"{' '.join(display)}")

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life")
        lives -= 1

        if lives == 0:
            game_is_finished = True
            print("You Lose!")

    if "_" not in display:
        game_is_finished = True
        print("You win")

    print(stages[lives])
