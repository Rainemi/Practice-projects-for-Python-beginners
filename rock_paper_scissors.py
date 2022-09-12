
import random
exit = False
user_points = 0
computer_points = 0

while exit == False:
    options = ["rocks", "paper" "scissors"]
    user_input = input("Choose rock, paper, scissors or exit: ")
    computer_input = random.choice(options)

    if user_input == "exit":
        print("Game Ended")
        print("You won a total score of " +  str(user_points) +"and the compuer won a total score of "+ str(computer_points))
        exit= True

    if user_input == "rock":
        if computer_input == "rock":
            print("It is a tie")
            print("both you and the computer input rock")
        elif computer_input == "paper":
            print("Your input is rock, computer input is paper")
            print("Computer wins")
            computer_points += 1
        elif computer_input == "scissors":
            print("Your input is rock, computer input is scissors")
            print("You win")
            user_points += 1
    
    elif user_input == "paper":
        if computer_input == "rock":
            print("You win")
            print("Your input is paper computer input is rock")
            user_points += 1
        elif computer_input == "paper":
            print("Your input is paper, computer input is paper")
            print("it is a tie")
        elif computer_input == "scissors":
            print("Your input is paper, computer input is scissors")
            print("Computer wins")
            computer_points += 1

    elif user_input == "scissors":
        if computer_input == "rock":
            print("Computer wins")
            print("Your input is scissors and computer input is rock")
            computer_points += 1
        elif computer_input == "paper":
            print("Your input is scissors, computer input is paper")
            print("You win")
            user_points += 1
        elif computer_input == "scissors":
            print("Your input is scissors, computer input is scissors")
            print("It is a tie")
            user_points += 1
    elif user_input != "rock" or user_input != "paper" or user_input != "scissors":
        print("invalid input")
    
        

