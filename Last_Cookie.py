"""
LESSON: 2.4 - While Loops
EXERCISE: Last Cookie
"""

#### ---- VARIABLE SETUP ---- ####
print("Let's play Last Cookie! ")
print("Who will get the last cookie? ")
# Assign the value 16 to the variable cookies
cookies = 16

# Assign the value True to the variable player1_turn
# ---> TEST AFTER THIS LINE <--- #
player1_turn = True


#### ---- GAME LOOP ---- ####

# WHILE there are GREATER THAN 0 cookies
while cookies > 0:

    #### ---- TURN INFORMATION ---- ####

    # Print how many cookies are left
    print("There are " + str(cookies) + " cookies left in the jar ")

    # IF it is player1_turn
    if player1_turn:
        current_player = "Player 1"

        # Assign current_player the string "Player 1"


    # ELSE
    else:

        # Assign current_player the string "Player 2"
        current_player = "player 2"

    # Print that it is current_player's turn
    print(current_player + ", it's your turn. ")


    #### ---- COOKIE REMOVAL ---- ####

    # Ask the player how many cookies to take (1, 2, or
    # 3). Assign to the variable take_out_string.
    take_out_string = input("How many cookies do you want to take out? ")

    # Typecast take_out_string to an int. Assign the
    # result to the variable take_out.
    take_out = int(take_out_string)

    # Decrement cookies by take_out
    # ---> TEST AFTER THIS LINE <--- #
    cookies -= take_out


    #### ---- END OF TURN ---- ####

    # Print a blank line for spacing
    print("")

    # Assign player1_turn the value NOT player1_turn
    # ---> TEST AFTER THIS LINE <--- #
    player1_turn = not player1_turn


#### ---- FINAL OUTPUT ---- ####

# Print a win message using the current_player string
# ---> TEST AFTER THIS LINE <--- #
print("Congratulations, " + current_player + " you are the winner!")
print("")

# Turn in your Coding Exercise.





