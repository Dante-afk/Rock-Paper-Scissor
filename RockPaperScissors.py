from optparse import Option
from random import choices
from ssl import Options
from unittest import result
from urllib import response
import random
"""
just a greeting
def greetings():
    return  "Hello! Welcome to ROCK PAPER SCISSORS!"

response = greetings()
print(response)
"""

#main code
#choices
def get_choices():
    player_choice = input("Enter a choice (rock, paper, scissors):")
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}  #dictionary
    return choices

def check_win(player, computer):
    print(f"You chose {player} and the computer chose {computer}")
    if player == computer:
        return "It's a TIE!"
    elif player == "rock":
      if computer == "scissors":
        return "You WIN!"
      else:
        return "You LOSE!"
    elif player == "paper":
      if computer == "rock":
        return "You WIN!"
      else:
        return "You LOSE!"
    elif player == "scissors": 
      if computer == "paper":
        return "You WIN!"
      else:
        return "You LOSE!"

choices = get_choices()  
result = check_win(choices["player"], choices["computer"])
print(result)


