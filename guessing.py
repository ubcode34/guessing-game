import random
  # Imports the random module to generate random numbers.

random_number = random.randint(1, 10) 
 # Generates a random number between 1 and 10.
previous_guesses = [] 
 # Creates an list to store the player's guesses.
correct_answer_picked = False 
 # Keeps the game playing until the player guesses correctly.

while not correct_answer_picked: 
     # Repeats the game until the correct number is guessed.
    user_guess = int(input("Enter a number between 1 - 10: "))
      # Asks the player for a guess between 1 - 10.

    while user_guess < 1 or user_guess > 10 or user_guess in previous_guesses:
          # Checks whether the guess is outside the range or has already been guessed.
        if user_guess < 1 or user_guess > 10:
              # Checks whether the guess is outside the allowed range.
            print("Invalid input!") 
             # Tells the player that the number is outside the range.
        else:  
            # Runs when the number is in range but has already been guessed.
            print("You already guessed", user_guess, "!") 
             # Tells the player that the guess is a duplicate.
            print("Choose a different number.")
              # Asks the player to choose another number.
            print("Previous guesses:", previous_guesses) 
             # Displays the guesses already made.

        user_guess = int(input("Enter a number between 1 - 10: "))
          # Asks for another guess until it passes validation.

    previous_guesses.append(user_guess) 
     # Adds the valid, new guess to the list.

    if user_guess == random_number: 
         # Checks whether the player's guess matches the random number.
        correct_answer_picked = True 
         # Ends the game loop because the player guessed correctly.
        print("You guessed correctly! The number was", random_number, ".") 
         # Congratulates the player and reveals the number.
        print("Your guesses:", previous_guesses)
          # Displays every valid guess, including the winning guess.

    elif user_guess > random_number: 
         # Checks whether the guess is greater than the random number.
        print("Try again! The random number is lower!") 
         # Tells the player to guess a lower number.
        print("Previous guesses:", previous_guesses)
          # Displays the guesses made so far.

    
    else:  
        # Runs when the guess is lower than the random number.
        print("Try again! The random number is higher!") 
         # Tells the player to guess a higher number.
        print("Previous guesses:", previous_guesses) 
         # Displays the guesses made so far.