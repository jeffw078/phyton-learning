#LEARNED HOW TO READ AND WRITE LINES IN TXT FILE
# arquivo = open("newfile.txt", "w")
# arquivo.write("Vaishyas")
# arquivo.close()

#ESCRITA
# with open("newfile.txt", "a") as arquivo:
#     arquivo.write("\nWrite line test")

#LEITURA

with open("newfile.txt", "r") as arquivo:
    for linha in arquivo.readlines():
        print(linha)


