"""A number-guessing game."""

import random

secret_number = random.randint(1, 100)
count = 0

name = input("Howdy! What's your name? ")
print(f"{name}, I'm thinking of a number between 1 and 100.")

# def verify_input():
#     while True:
#         try:
#             guess = int(input("Your guess? "))
#             if guess < 1 or guess > 100:
#                 print("Please input a number between 1 and 100.")
#             else:
#                 return guess
#         except:
#             print("Invalid input. Try again.")

# while True:
#     user_guess = verify_input()
#     count += 1

#     if user_guess < secret_number:
#         print("Too low. Try again.")
#     elif user_guess > secret_number:
#         print("Too high. Try again.")
#     else:
#         print(f"Congrats {name}. You got the correct number in {count} tries.")
#         break

guess = 0

def get_guess():
    while True:
        try:
            guess = int(input("Your guess? "))
            if guess > 100 or guess < 1:
                print("Please input a number between 1 and 100.")
            else:
                return guess
        except:
            print("Invalid number. Try again.")


def check_guess():
    while True:
        global count
        count += 1
        user_guess = get_guess()
        
        if user_guess < secret_number:
            print("Too low. Try again.")
        elif user_guess > secret_number:
            print("Too high. Try again.")
        else:
            print(f"Congrats {name}. You got the correct number in {count} tries!")
            break

check_guess()