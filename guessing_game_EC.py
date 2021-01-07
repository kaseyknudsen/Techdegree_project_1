import random


def start_game():

    scores = []

    random_number = random.randint(1, 10)
    attempt_count = 0

    while True:
        if attempt_count == 0:
            message = "Pick a number between 1 & 10, inclusive:  "
        elif user_guess not in range(1, 11):
                print("Your guess is outside of the range.")
        elif user_guess < random_number:
            message = "It's higher: "
        elif user_guess > random_number:
            message = "It's lower:  "
        else:
            break

        try:
            user_guess = int(input(message))
            attempt_count += 1                       
        except ValueError:
            print("Oops! That's not a valid number. Try again!")

    print("Woohoo! Congratulations! You won in {} attempts. Game over.".format(attempt_count))
    play_again = input("Would you like to play again? Y/N:  ")
    
    if play_again.lower() == 'y':
        print("Ok, great!")
        scores.append(attempt_count)
        print("Your best score so far is {}.".format(min(scores)))
        start_game()
    else:
        print("Ok, thanks for playing!")

start_game()
    
        
