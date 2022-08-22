import random # Importing Dependencies

def deal_card():
    """Returns a random card from the deck"""
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """Takes the list a cards and returns the score calculated from those cards. Also, detects a blackjack. Solves the issue of the value of Ace in specfic cases!"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, computer_score):
    """Compares the scores and gives the result"""
    if user_score > 21 and computer_score > 21:
        return "You went over. You Lose"

    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "You Lose. Opponent has a blackjack"
    elif user_score == 0:
        return "Win with a blackjack!"
    elif computer_score > 21:
        return "Opponent went over. You win!"
    elif user_score > 21:
        return "You went over. You Lose!"
    elif user_score > computer_score:
        return "You Win!"
    else:
        return "You Lose"

def main_game():
    print("Hi and welcome to blackjack!")

    # Fetching random cards from the deck for the user and the computer
    user_cards = [deal_card(), deal_card()]
    computer_cards = [deal_card(), deal_card()]

    # User Loop
    completed = False
    while not completed:
        # We are using hte calculate_score function to get the user_score and the computer_score
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        # Printing the initial step of cards
        print(f"Your cards: {user_cards} current score: {user_score}")
        print(f"Computers first card: {computer_cards[0]}")
        # Checking if the user has already lost the game in the first fetch
        if user_score == 0 or computer_score == 0 or user_score > 21:
            completed = True
        else:
            # If not, then we allow the user to fetch another card!
            cont = input(f" Type 'y' to get another card, type 'n' to pass: ")
        
            if cont == "y":
                user_cards.append(deal_card())
            elif cont == "n":
                # If the user says pass to the computer, then we stop the user loop
                completed = True

    # Computer's loop
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, You final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, Computer's final score: {computer_score}")
    print(compare(user_score, computer_score))

while input("Do you want to play the game of Blackjack? ") == "y":
    main_game()
