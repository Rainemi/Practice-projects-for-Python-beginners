#import random
#define a function to rol the dice
#crete a dictionary that will have drawings of the dice
#ask if user wants to conti ue running the program
#create a loop that'll loop through it if the user chooses to continue

import random

def roll_dice():
    roll = input("Roll the dice (Yes or No) ")

    while roll.lower() == "Yes".lower():
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)

        print("dice rolled : {} and {}".format(dice1,dice2))

        roll = input("Roll again ? (Yes/No): ")
roll_dice()