def menu_selection():
    return input("O que você deseja realizar?\n" +
                 "(I) - Para inserir um usuário\n" +
                 "(P) - Para Pesquisar um usuário\n" +
                 "(E) - Para Excluir um usuário\n" +
                 "(L) - Para listar os usuários\n" +
                 "ESCOLHA UMA DAS OPCOES: ").upper()


def listar(dicionario):
    with open("database.txt", "r") as arquivo:
        for linha in arquivo.readlines():
            print(linha)


def pesquisar(dicionario):
    pesquisarCPF = input("Digite um CPF: ")
    print(dicionario.get(pesquisarCPF))


def inserir(dicionario):
    dicionario[input("Digite o CPF: ").upper()] = [
        input("Digite o nome: ").upper(),
        input("Digite a data de nascimento: "),
        input("Digite o seu estado: ")]

    salvar(dicionario)

def salvar(dicionario):
    with open("database.txt", "a") as arquivo:
        for chave, valor in dicionario.items():
            arquivo.write(chave + ":" + str(valor) + "\n")

def excluir(dicionario):
    delete_cpf = input("Digite um CPF: ")
    with open("database.txt", "r") as f:
        lines = f.readlines()
    with open("database.txt", "w") as f:
        for line in lines:
            if not line.startswith(delete_cpf):
                f.write(line)

