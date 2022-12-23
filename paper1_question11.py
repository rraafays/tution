options = ["paper", "rock", "scissors"]
player1 = input()
player2 = input()
player1HasWon = False
draw = False
if player1 == 1:
    if player2 == 2:
        player1HasWon = True
if player1 == 2:
    if player2 == 3:
        player1HasWon = True
if player1 == 3:
    if player2 == 1:
        player1HasWon = True

if player1 == player2:
    draw = True

if (player1HasWon):  # if (player1HasWon == True)
    print("player 1 wins")
if (draw):  # if (draw == True)
    print("draw")
else:
    print("player 2 wins")
