import random

items = ["rock", "paper", "scissors"]

YourScore = 0
BotScore = 0
print(items)
yourchoice = input("Enter your choice (rock, paper, scissors): ").lower()

#Enable for Debugging(e7na 3eyal metnaka)
#print(choices)
while YourScore < 10 or BotScore < 10:
    
  
    while yourchoice not in items:
        print("Invalid input try again.")
        yourchoice = input("Enter your choice (rock, paper, scissors): ").lower()

    choices = random.choices(items)

    if yourchoice == choices:
                print("It's a tie!")
    elif ((yourchoice == "rock" and choices[0] == "scissors") or
          (yourchoice == "scissors" and choices[0] == "paper") or
          (yourchoice == "paper" and choices[0] == "rock")):

                 print("You won!")
                 YourScore += 1
                 yourchoice = input("Enter your choice (rock, paper, scissors): ").lower()

    else:
        print("You lost!")
        BotScore += 1
        yourchoice = input("Enter your choice (rock, paper, scissors): ").lower()

    print("Your Score", YourScore)
    print("Bot Score", BotScore)

    if YourScore == 10:
                print("Congrats!")
                break
    elif BotScore == 10:
                 print("Womp Womp, try again!")
                 break



