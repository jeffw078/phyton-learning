#THIS IS THE FINAL PROJECT AFTER 1 MONTH OF STUDY ABOUT PYTHON
#WRITING USER DATA, AFTER WE CAN READ OR DELETE THIS DATA WICH IS STORED IN TXT FILE

#IN THIS PROJECT I USED WHOLE CONTENT LEARND DURING THE TIME
#SUCH AS LOOPS, IF STATEMENT, FUNCTIONS, TUPLES, LISTS AND SO


from functions import menu_selection, inserir, listar, excluir, pesquisar

usuarios = {}
opcao = menu_selection()
while opcao == "I" or opcao == "P" or opcao == "E" or opcao == "L":
    if opcao == "I":
        inserir(usuarios)
    elif opcao == "L":
        listar(usuarios)
    elif opcao == "E":
        excluir(usuarios)
    else:
        pesquisar(usuarios)

    opcao = menu_selection()