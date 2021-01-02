

import random

def start_game():
    while True:
        try:
            user_guess = int(input("Hello friend! Please guess a number between 1 and 10, inclusive:  "))
            random_number = (random.randint(1, 10))
            random_number = int(random_number)
            attempt_count = 1
        except ValueError:
            print("Oops! Not a valid value. Try again.")
        
        else:      
            while user_guess != random_number:
                attempt_count += 1
                try:
                    if user_guess < random_number:
                        user_guess = int(input("It's higher:  "))
                    if user_guess > random_number:
                        user_guess = int(input("It's lower:  "))
                except ValueError:
                    print("Oops! Not a valid value. Try again.")       
            else:        
                print("Woo hoo! Congratulations! You got it!")
                print("Number of attempts: {}. Game over!".format(attempt_count))
                break

start_game()
