print("Let's play Last Cookie! ")
print("Who will get the last cookie? ")
cookies = 16

player1_turn = True

while cookies > 0:
    print("There are " + str(cookies) + " cookies left in the jar ")

    if player1_turn:
        current_player = "Player 1"

    else:
        current_player = "player 2"

    print(current_player + ", it's your turn. ")
    take_out_string = input("How many cookies do you want to take out? ")
    take_out = int(take_out_string)
    cookies -= take_out

    print("")
    player1_turn = not player1_turn

print("Congratulations, " + current_player + " you are the winner!")
print("")
