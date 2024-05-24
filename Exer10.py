table = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]


print("\n    1   2   3")
print("A | - | - | - |")
print("  -------------")
print("B | - | - | - |")
print("  -------------")
print("C | - | - | - |\n")

def isMovePlayed(prompt):
    while True:
        playerXPos = input(prompt)
        cordsX = playerXPos.split(",")
        cordsX[0] = ord(cordsX[0].lower()) - 97
        cordsX[1] = int(cordsX[1]) - 1  
        if not(cordsX in playedMoves):
            break

def checkWinner(player):
    winnerPlayer = 0
    for row_col in range(3):
        vertical = abs(table[0][row_col] + table[1][row_col] + table[2][row_col]) == 3
        horizontal = abs(table[row_col][0] + table[row_col][1] + table[row_col][2]) == 3

        if vertical or horizontal:
            winnerPlayer = player
            break
    
    diagonal = abs(table[0][0] + table[1][1] + table[2][2]) == 3 or abs(table[0][2] + table[1][1] + table[2][0]) == 3
    if diagonal:
        winnerPlayer = player
    
    if winnerPlayer != 0:
        if winnerPlayer == 1:
            print("Jogador X ganhou!")
        elif winnerPlayer == -1:
            print("Jogador O ganhou!")

    return winnerPlayer


def moveToBoard(player, prompt):
    winner = 0
    playerPos = input(prompt)
    cords = playerPos.split(",")
    cords[0] = ord(cords[0].lower()) - 97
    cords[1] = int(cords[1]) - 1
    if cords in playedMoves:
        print("Movimento ja jogado!")
        isMovePlayed(prompt)

    table[cords[0]][cords[1]] = player
    playedMoves.append(cords)
    winner = checkWinner(player)
    return winner

playedMoves = []
playedRounds = 0
while True:
    playerWon = 0

    # PLAYER X
    promptX = "Digite a posição do X (ex. A, 1): "
    playerWon = moveToBoard(1, promptX)
    playedRounds += 1
    if playerWon != 0:
        break

    if playedRounds >= 9:
        print("Empate!")
        break

    # PLAYER O
    promptO = "Digite a posição do O (ex. C, 3): "
    playerWon = moveToBoard(-1, promptO)
    playedRounds += 1
    if playerWon != 0:
        break