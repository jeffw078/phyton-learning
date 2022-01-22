#GENERATE A RANDOM PASSWORD WITH 12 CHARACTERS IN A TXT FILE

from random import randint
elements = "!@#$%^&*(){}|\/*-+=;.,?~ABDEFGHIJKLMONOPQRSTUVXWYZABDEFGHIJKLMONOPQRSTUVXWYZ1234567890,"
characters = len(elements)

password = ""
while len(password) < 12:
  pos = (randint(0, characters))
  password = password + (elements[pos])

password_file = open("data.txt", "a")
password_file.write("\n"+ password)
password_file.close()
