############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:

import random 
from replit import clear
from art import logo



# returning a random item from cards as value for
# deal_card() once it is called 
def deal_card():    
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  random_card = random.choice(cards)
  return random_card




def calculate_score(cards):
  card_sum = sum(cards)
  card_length = len(cards)
  if card_sum == 21 and card_length == 2:
    # 0 represents a winning score (blackjack)
    return 0
  if 11 in cards and card_sum > 21:
    cards.remove(11)
    cards.append(1)

  return card_sum


def compare_cards(user_score, computer_score):
  if user_score == computer_score:
    print("It's a draw! 😅")
  elif user_score == 0:
    print("Blackjack! You win! 🏆")
  elif computer_score == 0:
    print("You lose...😭🖕")
  elif user_score > 21:
    print("You went over, you lose...😭🖕")
  elif computer_score > 21:
    print("Computer went over, you win! 🏆")
  else:
    if user_score > computer_score:
      print("You win! 🏆")
    elif computer_score > user_score:
      print("You lose...😭🖕")



# starts game of blackjack
def play_game():
  print(logo)
  user_cards = []
  computer_cards = []
  is_game_over = False


# for loop to append 2 instances of deal_card() to
# user_cards and computer_cards  
  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())


  while not is_game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"Your cards: {user_cards}\nYour score: {user_score}\n")
    print(f"The computers first card: {computer_cards[0]}\n")

    if user_score == 0 or computer_score == 0 or user_score > 21:
      is_game_over = True
    else:
      user_deal_again = input("Should we deal another round? 'y' or 'n' ")
      if user_deal_again == 'y':
        # Add another random card to user_cards list
        user_cards.append(deal_card())
      else:
        is_game_over = True

  while computer_score != 0 and computer_score < 17:
    # add new card to computers hand
    computer_cards.append(deal_card())
    # calculate new computer score
    computer_score = calculate_score(computer_cards)
  print(f"Your final hand is: {user_score}")
  print(f"Computers final hand is: {computer_score}\n")
  compare_cards(user_score, computer_score)

while input("\nWould you like to play a game of blackjack? 'y' or 'n': ") == 'y':
  clear()
  play_game()

## The cards in the list have equal probability of being drawn.

## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.



