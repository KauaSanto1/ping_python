import ipaddress
import socket
import os

# Exibe o menu de opções
print(" Menu ")
print("Escolha uma opção: ")
print("1 - Hostname, IP e Máscara da máquina")
print("2 - Verificar se máquina está disponível")
print("3 - Scanner de Portas")
print("0 - Sair")
op = int(input("Opção: "))

# Opção 1: Mostra o nome da máquina, IP e máscara de rede
if(op == 1):
    nomeMaquina = socket.gethostname()
    ip = socket.gethostbyname(nomeMaquina)
    print("Nome da máquina:", nomeMaquina)
    print("IP:", ip)
    mascara = ipaddress.IPv4Network(ip).netmask
    print("Máscara de rede:", mascara)

# Opção 2: Verifica se a máquina está disponível por IP ou URL
elif (op == 2):
    print("Escolha uma opção: ")
    print("1 - IP")
    print("2 - URL")
    op2 = int(input("Opção: "))

    if (op2 == 1):
        ip = input("Digite o IP: ")
        response = os.system("ping -c 1 " + ip)
        if response == 0:
            print("Ping feito com sucesso!")
        else:
            print("Falha no ping!")
    elif (op2 == 2):
        url = input("Digite a URL: ")
        response = os.system("ping -c 1 " + url)
        if response == 0:
            print("Ping feito com sucesso!")
        else:
            print("Falha no ping!")
    else:
        print("Opção inválida")

# Opção 3: Scanner de portas abertas
elif (op == 3):
    print("Verificação de portas abertas por IP ou URL")
    ip = input("Digite o IP ou URL: ")

    for porta in range(0, 1000):
        client = socket.socket()
        client.settimeout(0.05)

        if client.connect_ex((ip, porta)) == 0:
            print("A porta", porta, "está aberta")

# Opção 0: Sair do programa
elif (op == 0):
    print("Programa finalizado!")

# Caso o usuário escolha uma opção inválida
else:
    print("Opção inválida")
