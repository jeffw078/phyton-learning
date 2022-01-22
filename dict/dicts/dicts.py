#LEARNED ABOUT DICTS STORING DATA LOCALY HANDLING WITH USER INPUTS

usuarios = {}

usuarios = {"07863639913" : ["Jefferson Willian Cardoso", "07/08/1991", "São Bento do Sul", "Santa Catarina"],
            "06486459913" : ["Raquel Machado Fragoso", "25/04/1989", "São Bento do Sul", "Santa Catarina"]
            }
print("----####--CADASTRO--####----")
cpfCadastro = input("Digite seu CPF: ")
nomeCadastro = input("Digite seu nome completo: ")
nascCadastro = input("Digite sua data de Nascimento 00/00/0000: ")
cidadeCadastro = input("Digite sua cidade: ")
estadoCadastro = input("Digite seu estado: ")

usuarios[cpfCadastro] = [nomeCadastro,nascCadastro, cidadeCadastro, estadoCadastro]


print("\n" + str(usuarios))