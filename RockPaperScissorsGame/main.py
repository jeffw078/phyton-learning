#ROCK/PAPER/SCISSORS GAME
#STORING SCORE WHILE REPEAT STRUCTURE
#IF ELIF STATEMENT

import random
ttt = ["r", "p", "s"]
score_machine = 0
score_player = 0
tie = 0
player_name = input("Digite seu nome: ")
muchTimes = int(input("Quantas rodadas? "))
while muchTimes != 0:
    machine_choose = (random.choice(ttt))
    player_choose = input("BEST OF " + str(muchTimes) + "!\nMAKE YOUR CHOICE:\n(R)Rock\n(P)paper\n(S)Scissors\n")
    if player_choose == "r" and machine_choose == "p":
        score_machine += 1
    elif player_choose == "r" and machine_choose == "s":
        score_player += 1
    elif player_choose == "p" and machine_choose == "r":
        score_player += 1
    elif player_choose == "p" and machine_choose == "s":
        score_machine += 1
    elif player_choose == "s" and machine_choose == "r":
        score_machine += 1
    elif player_choose == "s" and machine_choose == "p":
        score_player += 1
    elif player_choose == machine_choose:
        tie += 1
    elif player_choose != "r" and player_choose != "p" and player_choose != "s":
        print("ENTRADA INVALIDA - TENTE NOVAMENTE")
    muchTimes = muchTimes - 1

# print(player_choose + "/" + machine_choose)
if score_player > score_machine:
    print("YOU WIN!")
else:
    print("YOU LOOSE!")

print("-/-/-/-/-/-/-/-/-/-/-/-/-/-RESULT-/-/-/-/-/-/-/-/-\n"  + str(player_name + " ") + str(score_player) + " x " + str(score_machine) + " Machine and " + str(tie) + " ties")





