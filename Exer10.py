table = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]


print("\n   1  2  3\nA [0, 0, 0]\nB [0, 0, 0]\nC [0, 0, 0]\n")

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

def isMovePlayed(prompt):
    while True:
        playerXPos = input(prompt)
        cordsX = playerXPos.split(",")
        cordsX[0] = ord(cordsX[0].lower()) - 97
        cordsX[1] = int(cordsX[1]) - 1  
        if not(cordsX in playedMoves):
            break

def moveToBoard():
    winner = 0
    playerXPos = input(promptX)
    cordsX = playerXPos.split(",")
    cordsX[0] = ord(cordsX[0].lower()) - 97
    cordsX[1] = int(cordsX[1]) - 1
    if cordsX in playedMoves:
        print("Movimento ja jogado!")
        isMovePlayed(promptX)

    table[cordsX[0]][cordsX[1]] = 1
    playedMoves.append(cordsX)
    print(playedMoves)
    winner = checkWinner(1)
    return winner

playedMoves = []
while True:
    playerWon = 0

    # PLAYER X
    promptX = "Digite a posição do X (ex. A, 1): "
    playerWon = moveToBoard()
    if playerWon != 0:
        break
    

    # PLAYER O
    promptO = "Digite a posição do O (ex. C, 3): "
    playerOPos = input(promptO)
    cordsO = playerOPos.split(",")
    cordsO[0] = ord(cordsO[0].lower()) - 97
    cordsO[1] = int(cordsO[1]) - 1
    if cordsO in playedMoves:
        print("Movimento ja jogado!")
        isMovePlayed(promptO)

    table[cordsO[0]][cordsO[1]] = -1
    playedMoves.append(cordsO)
    playerWon = checkWinner(-1)
    if playerWon != 0:
        break
