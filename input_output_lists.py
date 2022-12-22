leaderboard = []  # empty string array called leaderboard

player1 = input("who is player 1? ")  # asks who is player 1
player2 = input("who is player 2? ")  # asks who is player 2

for i in range(10):  # for in range 10
    winner = input("Who is the winner? ")  # prompts for the winner and input to the variable called winner
    leaderboard.append(winner)  # add the winner to the list

print("player 1 got " + str(leaderboard.count(player1)))  # writes the score of player 1
print("player 2 got " + str(leaderboard.count(player2)))  # writes the score of player 2

if player1 == player2:  # if player 1 draws with player 2 (their scores are the same)
    print("draw")  # tell them that they drew

if player1 > player2:  # if player 1's score is higher than player 2's
    print("player 1 wins")  # tell them player 1 won

if player1 < player2:  # if player 1's score is less than player 2's
    print("player 2 wins")  # tell them player 2 won
