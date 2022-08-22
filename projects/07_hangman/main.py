import random

words = ["help", "sequence", "computer", "frequence"]
guesses = 8 
word = random.choice(words)
guessed = []
complete = False
for letters in word:
        guessed.append("_")
while not complete:
    letter = input(f"you have {guesses} insert letter or word: ")
    for pos in range(len(word)):
        if word[pos] == letter:
            letter = guessed[pos]
    if letter not in word:
        guesses -= 1
        print(f"you have {guesses} left")
    elif guesses == 0:
        print(f"you lose")
    else: 
        print("you win")
    complete = True
