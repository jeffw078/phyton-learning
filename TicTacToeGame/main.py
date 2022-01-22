#ITS A SIMPLE TIC TAC TOE GAME BUILD WITH KNOWLEDGE AFTER 1 MONTH OF STUDY

import random
tablePositions = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
playerNumbers = []
computerNumbers = []

tableGame = str(("_1_|_2_|_3_\n"
                 "_4_|_5_|_6_\n"
                 "_7_|_8_|_9_\n"))

print(tableGame)
while len(tablePositions) >= 0:
    print(playerNumbers)
    print(computerNumbers)
    playerPosition = str(input("Escolha uma posição: "))
    playerNumbers.append(playerPosition)
    tablePositions.remove(playerPosition)
    computerChoice = random.choice(tablePositions)
    computerNumbers.append(computerChoice)
    tableGame = tableGame.replace(playerPosition, "❎")
    tableGame = tableGame.replace(computerChoice, "Ⓜ")
    playerWin = ["1", "2", "3"] or ["4", "5", "6"] or ["7", "8", "9"] or ["1", "5", "9"] or ["3", "5", "7"] in playerNumbers
    computerWin = ["1", "2", "3"] or ["4", "5", "6"] or ["7", "8", "9"] or ["1", "5", "9"] or ["3", "5", "7"] in computerNumbers
    print(playerWin)
    print(computerWin)

    print(tablePositions)
    print(tableGame)