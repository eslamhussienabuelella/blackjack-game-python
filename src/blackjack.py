
# -------------------------
# Deck & card utilities
# -------------------------

# Defining the card set of the game
import numpy as np
basic_cards = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
# simulating 52 card set without jokers
full_cards = basic_cards*4
# defining score calculator function


def score_calculator(hand_cards, role):
    """Calculate total score for cards based on role (player/dealer)."""
# Compute non-Ace card values for dealer and player
    score = []
# Create a copy of hand_cards before rearranging "Ace" cards to display to the player 
    hand_cards_view = hand_cards[:]
# Move all "Ace" cards to the end to ensure non-Ace cards are recorded before "Ace" cards

    ordered_hand = [card for card in hand_cards if card != "Ace"] + ["Ace"] * hand_cards.count("Ace")
    for card in ordered_hand:
        if card in ["Jack", "Queen", "King"]:
            score.append(10)
        elif card in ["2", "3", "4", "5", "6", "7", "8", "9", "10"]:
            score.append(int(card))
# Handling Ace values (1 or 11 )
        else:
# prompt player to choose (1 or 11).
            if role == "player":
                print("Your cards", hand_cards_view)
                Ace_value = int(input("You got Ace, Please choose your score 1 or 11: "))
# validate player's input is either 1 or 11                
                if Ace_value in [1,11]:
                    score.append(Ace_value)
                else:
                    while Ace_value not in [1,11]:
                        print("Invalid 'Ace' value please choose 1 or 11")
                        Ace_value = int(input("You got Ace, Please choose your score 1 or 11: "))
                        # score.append(Ace_value)
# Auto-assign Ace value for dealer based on current score
            elif role == "dealer":
# Loop to handle multiple Aces for the dealer
                for Ace in range(hand_cards.count("Ace")):
                    if sum(score) + 11 <= 21:
                        score.append(11)
                    else:
                        score.append(1)
# calculate the total score for the cards in hands
    total_score = sum(score)
# Score evaluation logic
# Returns 'Bust' if score exceeds 21
    if total_score>21:
        score_evaluation = "Bust"
# Return 'Black Jack' if score is 21 with exactly 2 cards (i.e initial draw)
    elif total_score==21 and len(hand_cards)==2:
        score_evaluation = "Black Jack"
# Otherwise, return the current score
    else:
        score_evaluation = "Neither Bust nor Black Jack"    
    return (total_score, score_evaluation)

# defining hit logic for dealer/player
def draw_logic(table_cards, cards_in_hand, role, draw_size):
    """draw logic for each role (player/dealer)."""
# Draw random card from thedeck cards.
# tolist to to convert to list not array
    hit = (np.random.choice(table_cards, size=draw_size, replace=False)).tolist()
    for card_index in range(draw_size):
# [0] to retrieve the value from the list
# Update remaining cards after each removal to ensure card will not be drawn more than 4 times
        table_cards.remove(hit[card_index])
        remaining_cards = table_cards
# Append the drawn (hitted) card to card in player's/ dealer's hands
        cards_in_hand.append(hit[card_index])
# Calculate score for the drawn cards by using the earlier function score_calculator
    cards_in_hand_score, score_evaluation = score_calculator(cards_in_hand, role)
    return(cards_in_hand,cards_in_hand_score,remaining_cards, score_evaluation)
table = full_cards[:]
def black_jack_logic():
    """Simulate one round of Blackjack and decide winner."""
# Create a fresh copy of the original card set for this round
    deck = full_cards.copy()
# Give 2 cards to player/dealer and get score and updated deck
    player_cards, player_score, deck, player_score_evaluation = draw_logic(deck,[], "player",2)
    dealer_cards, dealer_score, deck, dealer_score_evaluation = draw_logic(deck, [],"dealer",2)
# Display player's initial hand and score
    print("Player cards:", player_cards, "Score:", player_score)
# Show only the second card of the dealer's cards (the other hidden) as per Black Jack rules on wiki how
    print("Dealer shows:", ["*", dealer_cards[1]])
# Announce early winner/loser if Black Jack / Bust existed
    if player_score_evaluation == "Black Jack":
        print("Player got Blackjack!")
        print("Player wins")
        return ("Player wins", "Player got Blackjack!","Player score",player_score,"Dealer score",dealer_score)
    elif dealer_score_evaluation == "Black Jack":
        print("Dealer got Blackjack!")
        print("Dealer cards",dealer_cards)
        print("Dealer wins")
        return ("Dealer wins", "Dealer got Blackjack!","Player score",player_score,"Dealer score",dealer_score)
    elif player_score_evaluation == "Bust":
        print("Player busts!")
        print("Dealer wins")
        return ("Dealer wins","Player busts!","Player score",player_score,"Dealer score",dealer_score)
    elif dealer_score_evaluation == "Bust":
        print("Dealer busts!")
        print("Player wins")
        return ("Player wins", "Dealer busts!", "Player score",player_score,"Dealer score",dealer_score)    
# Ask the player to hit or stand in case no Black Jack or Busts existed
# .strip().lower() to handle space/ capital letters
    choice = input("Do you want to 'hit' or 'stand'? ").strip().lower()
# Continue hitting as long as player chooses to hit using while loop
    while choice == "hit":
# Draw a card and update player’s hand and score using the predefined hit_logic function
            player_cards, player_score, deck, player_score_evaluation_hit= draw_logic(deck, player_cards, "player",1)
# Show updated hand and score
            print("Player cards:", player_cards, "Score:", player_score)
# Check if player's new cards score is Bust
            if player_score_evaluation_hit == "Bust":
                print("Player busts!")
                print("Dealer wins")
# if the player got Bust the game will terminate and the dealer when
                return ("Dealer wins", "Player busts!","Player score",player_score,"Dealer score",dealer_score)
# Ask player for next move: hit or stand
            choice = input("Do you want to 'hit' or 'stand'? ").strip().lower()
# Show dealer's cards and start dealer's turn
    print("\nDealer reveals:", dealer_cards)
# Iterate dealer turn until the dealer's score is 17 or more
    while dealer_score < 17:
# Draw a card and update dealer's hand and score using the predefined hit_logic function
        dealer_cards, dealer_score, deck, dealer_score_evaluation_hit = draw_logic(deck, dealer_cards, "dealer",1)
# Show dealer's updated cards and score
        print("Dealer hits:", dealer_cards, "Score:", dealer_score)
# Check if dealer's new cards score is Bust
        if dealer_score_evaluation_hit == "Bust":
            print("Dealer busts!")
            print("Player wins")
            return ("Player wins", "Dealer busts!", "Player score",player_score,"Dealer score",dealer_score)
# Show both player's & dealer's cards after all actions without Busts or Black Jack
    print("\nFinal hands:")
# Show player's final cards and score
    print("Player:", player_cards, "Score:", player_score)
# Show dealer's final cards and score
    print("Dealer:", dealer_cards, "Score:", dealer_score)
# compare scores of dealer & player to announce the winner
    if player_score > dealer_score:
        print("Player wins")
        return ("Player wins", "Score based","Player score",player_score,"Dealer score",dealer_score)
    elif dealer_score > player_score:
        print("Dealer wins")
        return ("Dealer wins", "Score based","Player score",player_score,"Dealer score",dealer_score)
# handles the special case if dealer's & player's scores are equal 
    else:
        print("It's a tie!")
        return ("It's a tie!", "Score based","Player score",player_score,"Dealer score",dealer_score)
# Define the main Black Jack game interface function 
def play_black_jack():
    """Play multiple Blackjack rounds, report the results."""
# Initial condition variable for the game triggering/stopping. 
    play = "yes"
# Counter track total number of games played for summary display
    games = 0
# List to store the winner of each round
    winner_list = []
    results_table = []
# Continue game loop while user wants to play
    while play == "yes":
# Play one round and get the result ("Dealer wins","Player wins","It's a tie!")
        winner = black_jack_logic()
# Append the round result in the winner list
        winner_list.append(winner[0])
        results_table.append(winner)
# Increment games counter for each played round
        games+=1
# Ask the player whether to play another round or not.
        play = input("Do you want to play another round? (yes/no): ").strip().lower()
# Return total game rounds played, number of dealer wins, number of player wins, and number of ties
    return(results_table, games,winner_list.count("Dealer wins"), winner_list.count("Player wins"), winner_list.count("It's a tie!"))
# Call the function play_black_jack and assign the outputs to variables


if __name__ == "__main__":
    results_table, games, dealer_wins, player_wins, ties = play_black_jack()

    print("\nGame Results Table\n")
    for black_jack_round in results_table:
        print("Round", results_table.index(black_jack_round) + 1, black_jack_round)

    print(
        f"\nGame summary\nYou played {games} games:\n"
        f"Dealer won {dealer_wins} times\n"
        f"Player won {player_wins} times\n"
        f"Game was tied {ties} times"
    )


