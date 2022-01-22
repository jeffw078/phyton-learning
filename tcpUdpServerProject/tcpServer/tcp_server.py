from socket import *

# resp="S"
#
# while(resp=="S"):
#     url=input("Digite uma URL: ")
#     ip=socket.gethostname(url)
#     print("O IP referente a URL informada é: ", ip)
#     resp=("Digite <S> para continuar: ").upper()

# portas 0 ate 65535

servidor="127.0.0.1"
porta=43210

obj_socket = socket(AF_INET, SOCK_STREAM)
obj_socket.bind((servidor,porta))
obj_socket.listen(2)

print("Aguardando cliente...")

while True:
    con, cliente = obj_socket.accept()
    print("Conectado com: ", cliente)
    while True:
        msg_recebida = str(con.recv(1024))
        print("Recebemos: ", msg_recebida)
        msg_enviada = b'Olah Cliente'
        con.send(msg_enviada)
        break
    con.close()

