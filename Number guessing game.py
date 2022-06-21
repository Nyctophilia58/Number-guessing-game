import random
import time
from statistics import mean, mode, median

print("*" * 50, "\n" + " "*5, "Welcome to my number guessing game!!! ".upper(), "\n" + "*" * 50, "\n")
name = (input("What is your name? ")).title()

print(f"Hello {name}, this a simple game. "
      f"I'll choose a random number between 0 and 100 inclusive and you have to guess the number right. ")
attempt_list = []

decision = input("Are you ready to play? Y/N ")
if decision.lower() == 'y':
    print("Let's begin the game. ")
    random_num = random.randint(0, 100)
    Quit = True
    count = 0
    while Quit:
        count = count + 1
        try:
            user_num = int(input("Guess a number: "))
        except ValueError:
            print("Invalid number, try again! ")
            count = 0
            continue
        if (user_num > 100) | (user_num < 0):
            print("The number is out of range. Please try again. ")
        elif random_num == user_num:
            print("\nYAY!! You've guessed the right number. ")
            print(f"It took you {count} times to get it right.")
            attempt_list.append(count)
            Quit = False
            print(f"The mean of the saved attempts list is: {mean(attempt_list)}")
            print(f"The median of the saved attempts list is: {median(attempt_list)}")
            print(f"The mode of the saved attempts list is: {mode(attempt_list)}")
            decision = input(f"\nDo you want to play again? Y/N ")
            if decision.lower() == "y":
                print(f"The current best score is: {min(attempt_list)}\n")
                count = 0
                Quit = True
                random_num = random.randint(0, 100)
            else:
                Quit = False
        elif random_num > user_num:
            print("Your answer should be higher. ")
        else:
            print("Your answer should be lower. ")
    print("Thanks for playing :) ")
    time.sleep(1.5)
else:
    print("Ok. Thanks for playing our game. ")
    time.sleep(1.5)
