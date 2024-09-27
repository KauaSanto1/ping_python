import os
import platform

# Definindo o comando para limpar a tela, dependendo do sistema operacional
cls = 'cls' if platform.system().lower() == 'windows' else 'clear'

# Exibe o menu de opções
print("Menu Teste Conexão")
print("Opções: ")
print("Teste IP : 1")
print("Teste URL: 2")
op = int(input("Digite a opção desejada: "))

# Teste de conexão por IP
if (op == 1):
    os.system(cls)
    ip = input("Digite o IP: ")
    response = os.system("ping -c 1 " + ip)
    if response == 0:
        os.system(cls)
        print("Teste concluído com sucesso!!")
    else:
        os.system(cls)
        print("Não foi possível estabelecer conexão com o IP escolhido!!")

# Teste de conexão por URL
elif (op == 2):
    os.system(cls)
    url = input("Digite a URL: ")
    response = os.system("ping -c 1 " + url)
    if response == 0:
        os.system(cls)
        print("Teste concluído com sucesso!!")
    else:
        os.system(cls)
        print("Não foi possível estabelecer conexão com a URL escolhida!!")

# Caso o usuário escolha uma opção inválida
else:
    os.system(cls)
    print("DIGITE UMA OPÇÃO VÁLIDA!")
