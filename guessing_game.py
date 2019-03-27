# """
# Python Web Development Techdegree
# Project 1 - Number Guessing Game
# --------------------------------
# 
# For this first project we will be using Workspaces. 
# 
# NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.
# 
# """
# 
#     """Psuedo-code Hints
#     
#     When the program starts, we want to:
#     ------------------------------------
#     1. Display an intro/welcome message to the player. - Line 34
#     2. Store a random number as the answer/solution. - Line 29
#     3. Continuously prompt the player for a guess. - Line 39-57
#       a. If the guess greater than the solution, display to the player "It's lower". - Line 54-57
#       b. If the guess is less than the solution, display to the player "It's higher". - Line 50-53
#     4. Once the guess is correct, stop looping, inform the user they "Got it"
#        and show how many attempts it took them to get the correct number. - Line 42-44
#     5. Let the player know the game is ending, or something that indicates the game is over. - Line 65
#     
#     ( You can add more features/enhancements if you'd like to. )
#     """

import random
while True:
    correct_number = random.randint(1, 10)
    number_of_tries = 1
    
    if __name__ == '__main__':
        def start_game():
            print("Hello and welcome to the game, guess a number between 1 and 10. The goal is to guess the correct number")
        
    
    while True:
        try:
            guess = int(input("Please enter a number between 1-10: "))
        # Make sure your script runs without errors. Catch exceptions and report errors to the user in a meaningful way.
        except ValueError:
            number_of_tries += 1
            print("Oops, guesses have to be number characters, other characters are not accepted by this program! Skynet has spoken :-) ")
            continue
        if guess == correct_number:
            print("Got it")
            break
    # As a player of the game, my guess should be within the number range. If my guess is outside the guessing range I should be told to try again.
        elif guess >= 11:
            number_of_tries += 1
            print("Please stay within 1-10 range of numbers")
            continue    
        elif guess <= correct_number:
            number_of_tries += 1
            print("It's higher")
            continue
        elif guess >= correct_number:
            number_of_tries += 1
            print("It's lower")
            continue
        
    print("Game over, it took {} tries GG".format(number_of_tries))
    # As a player of the game, after I guess correctly I should be prompted if I would like to play again.
    go_again = input("Do you wanna go for another round? (Y/N): ")
    if go_again.lower() =="y":
        start_game()
    else:
        print("Thank you for playing! ")
        break

# As a player of the game, at the start of each game I should be shown the current high score (least amount of points), so that I know what I am supposed to beat.