#IN THIS GAME USER MUST GUESS THE NUMBER COMPUTER CHOOSE BETWEEEN 0 AND 100
#USED WHILE LOOP, IF STATEMENT AND RAND METHOD

import random

rand = random.randint(0,100)
newbet = ""

while rand != newbet:
    newbet = int(input("Digite um número de 0 a 100: "))
    if newbet > rand:
     print("O número é menor!")
    elif newbet < rand:
     print("O número é maior")
    else:
     print("Você acertou!")
