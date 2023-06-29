import random

options = ["rock", "paper", "scissor"]

while True:
    comCount = 0
    userCount = 0
    userChoice = int(input(''' 
    Game Start..
    1 Yes
    2 No | Exit
    '''))
    
    if userChoice == 1:
        for a in range(1, 6):
            userInput = int(input('''
            1 Rock
            2 Paper
            3 Scissor
            '''))
            
            if userInput == 1:
                userChoice = "rock"
            elif userInput == 2:
                userChoice = "paper"
            elif userInput == 3:
                userChoice = "scissor"
            else:
                print("Invalid input")
                continue
            
            comChoice = random.choice(options)
            print("User Choice : ", userChoice)
            print("Computer Choice : ", comChoice)
            
            if comChoice == userChoice:
                print("Game Draw")
                userCount += 1
                comCount += 1
            elif (userChoice == "rock" and comChoice == "scissor") or (userChoice == "paper" and comChoice == "rock") or (userChoice == "scissor" and comChoice == "paper"):
                print("You win")
                userCount += 1
            else:
                print("Computer wins")
                comCount += 1

        # print("Final Score:")
        print("Computer Score:", comCount)
        print("User Score:", userCount)
        
        if userCount == comCount:
            print("Game Draw")
        elif userCount > comCount:
            print("User wins")
        else:
            print("Computer wins")

    elif userChoice == 2:
        break
