import random
from art import logo
import os

print(logo)

#Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#10 is King, Queen and Jack
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def deal_card():
  """Returns a random card from the deck."""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

#Create a function called calculate_score() that takes a List of cards as input and returns the score.
def calculate_score(dealt_cards):
    """Take a list of cards and return the sum of the cards"""
    if len(dealt_cards) == 2 and 10 in dealt_cards and 11 in dealt_cards:
      return 0
    else:
      cards_sum = sum(dealt_cards)
      #replace 11 with 1 if the sum is above 21
      if cards_sum > 21 and 11 in dealt_cards:
        dealt_cards.remove(11)
        dealt_cards.append(1)
      return cards_sum

#Create a play_game() function that will be called whenever the user wants to play the game
def play_game():
  user_cards = []
  computer_cards = []
  #Deal the user and computer 2 cards each using deal_card() and append().
  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
  
  print(f"Your cards are {user_cards} and the sum is {calculate_score(user_cards)}")
  print(f"Computer's first card is {computer_cards[0]}")
  
  #Check if they have a blackjack or the sum of their cards is above 21 or they want another card
  continue_playing = True
  while continue_playing:
    if calculate_score(computer_cards) == 0:
      print("Computer has a blackjack. You lose!")
    elif calculate_score(user_cards) == 0:
      print("You have a blackjack. You win!")
    elif calculate_score(user_cards) > 21:
      continue_playing = False
    else:
      if input("Do you want to draw another card? y or n: ") == "y":
        user_cards.append(deal_card())
        print(f"Your cards are {user_cards} and the sum is {calculate_score(user_cards)}")
      else:
        continue_playing = False
        print(f"Your cards are {user_cards}")
    
  #Once the user is done, the computer should keep drawing cards as long as it has a score less than 17.
  while calculate_score(computer_cards) < 17 and calculate_score(computer_cards) != 0:
    computer_cards.append(deal_card())
  
  #Create a function called compare() that will compare each player's cards and declare a winner
  def compare(user_score, computer_score):
    if user_score == computer_score:
      return("It is a draw!")
    # elif computer_score == 0:
    #   return("Computer has a blackjack. You lose!")
    # elif user_score == 0:
    #   return("You have a blackjack. You win!")
    elif user_score > 21:
      return("Your score is greater than 21. You lose!")
    elif computer_score > 21:
      return("Computer score is greater than 21. You win!")
    elif computer_score > user_score:
      return("Computer wins!")
    else:
      return("You win!")

  print(f"Computer's cards are {computer_cards}")
  print(compare(calculate_score(user_cards), calculate_score(computer_cards)))

#Ask the user if they want to play the game
while input("Do you want to play a game of Blackjack? y or n: ") == "y":
  os.system('cls')
  print(logo)
  play_game()

