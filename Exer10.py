table = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]


print("\n   1  2  3\nA [0, 0, 0]\nB [0, 0, 0]\nC [0, 0, 0]\n")

def checkWinner(player):
    winner = 0
    for row_col in range(3):
        vertical = abs(table[0][row_col] + table[1][row_col] + table[2][row_col]) == 3
        horizontal = abs(table[row_col][0] + table[row_col][1] + table[row_col][2]) == 3

        if vertical or horizontal:
            winner = player
            break
    
    diagonal = abs(table[0][0] + table[1][1] + table[2][2]) == 3 or abs(table[0][2] + table[1][1] + table[2][0]) == 3
    if diagonal:
        winner = player
    
    if winner != 0:
        if winner == 1:
            print("Jogador X ganhou!")
        elif winner == -1:
            print("Jogador O ganhou!")

    return winner

def isMovePlayed():
    while True:
        playerXPos = input("Digite a posição do X (ex. A, 1): ")
        cordsX = playerXPos.split(",")
        cordsX[0] = ord(cordsX[0].lower()) - 97
        cordsX[1] = int(cordsX[1]) - 1  
        if not(cordsX in playedMoves):
            break

playedMoves = []
while True:
    playerWon = 0

    playerXPos = input("Digite a posição do X (ex. A, 1): ")
    cordsX = playerXPos.split(",")
    cordsX[0] = ord(cordsX[0].lower()) - 97
    cordsX[1] = int(cordsX[1]) - 1
    if cordsX in playedMoves:
        print("Movimento ja jogado!")
        isMovePlayed()

    table[cordsX[0]][cordsX[1]] = 1
    playedMoves.append(cordsX)
    print(playedMoves)
    playerWon = checkWinner(1)
    if playerWon != 0:
        break
    
    playerOPos = input("Digite a posição do O (ex. C, 3): ")
    while playerOPos in playedMoves:
            print("Posição já ocupada!")
            playerOPos = input("Digite a posição do O (ex. C, 3): ")
    cordsO = playerOPos.split(",")
    cordsO[0] = ord(cordsO[0].lower()) - 97
    cordsO[1] = int(cordsO[1]) - 1
    if cordsO in playedMoves:
        print("Movimento ja jogado!")
        isMovePlayed()

    table[cordsO[0]][cordsO[1]] = -1
    playedMoves.append(cordsO)
    playerWon = checkWinner(-1)
    if playerWon != 0:
        break
