import random

items = ("rock", "paper", "scissors")

choices = random.choices(items)

YourScore = 0
BotScore = 0

#Enable for Debugging(e7na 3eyal metnaka)
#print(choices)

yourchoice = input("Enter your choice (rock, paper, scissors): ")

if yourchoice == choices[0]:
    print("It's a tie!")
if ((yourchoice == "rock" and choices[0] == "scissors") or
    (yourchoice == "scissors" and choices[0] == "paper") or
    (yourchoice == "paper" and choices[0] == "rock")):
    print("You won!")
else:
    print("You lost!")


