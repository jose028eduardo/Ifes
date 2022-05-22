# 1- Escolher um tema (biblioteca)
# 2- 6 campos
# 3- desenvolvimento em camadas:
# (arquivos, telas, inputs)
# (arquivos de persistência)
# 4- Utilizar CLS (limpa tela)
# 5- Uma tela para cada operação (CRUD)
# 6- Utilizar JSON como formato de dados.

# CRUD = Create, Read, Update, Delete



import os
import json
import time
import opcao1
import opcao2
import opcao3
import opcao4

bibliotecas = []

filename = "Lista_biblioteca.json"
def clear_console():
    os.system('cls')


clear_console()


def boas_vindas():
    print("Seja Bem-Vindo")
    time.sleep(2)
    while True:
        clear_console()
        print("Deseja continuar? S/N")
        confirmacao = input("")
        clear_console()
        confirmacaO = confirmacao.upper()
        if confirmacaO == "S":
            opcoes()
        elif confirmacaO == "N":
            print("Programa encerrado.")
            break
        elif confirmacaO != "S" and confirmacaO != "N":
            print("Opcão inválida, digite outra opção.")
            time.sleep(1.5)
            

    print("-"*30)


def opcoes():
    print("1- Cadastrar")
    print("2- Apagar")
    print("3- Visualizar")
    print("4- Atualizar")
    print("-"*30)
    opcao = (input("Digite a opção desejada:"))
    clear_console()
    funcoes(opcao)


def funcoes(opcao):
    if opcao == "1":
        opcao1.escolha1()
    elif opcao == "2":
        opcao2.opcao2()
    elif opcao == "3":
        opcao3.opcao3()
    elif opcao == "4":
        opcao4.opcao4()
    else:
        print("Opçao inválida, digite outro número.")
        time.sleep(2)

boas_vindas()




# def opcao1():
#     nome_biblioteca = input("Digite o nome da Biblioteca: ")
#     telefone = input("Digite o telefone da Biblioteca: ")
#     endereço = input("Digite o endereço: ")
#     publica = input("Diga se esta biblioteca é particular ou pública: ")
#     gerente = input("Digite o nome do(a) gerente: ")
#     tamanho = input("Digite o tamanho do acervo da biblioteca: ")
    
#     clear_console()

    
#     print("-"*30)
#     salvar = ({"nome_biblioteca": (nome_biblioteca), "telefone": (telefone), "publica": (
#         publica), "endereço": (endereço), "gerente": (gerente), "tamanho": (tamanho)})

    

#     print("Nome: ",salvar["nome_biblioteca"] )
#     print("Telefone: ",salvar["telefone"])
#     print("Endereço: ",salvar["endereço"])
#     print("Entidade pública ou privada: ",salvar["publica"])
#     print("Gerente:",salvar["gerente"])
#     print("Tamanho do acervo:",salvar["tamanho"])
#     print("-"*30)

#     print("O cadastramento está correto? Responda com S ou N.")
#     confirmaçao = input("Resposta: ")
#     while True:
#         if confirmaçao != "s" and confirmaçao != "S":

#             opcao1()
#         else:
#             clear_console
#             print("-"*30)
#             print("Finalizando cadastro...")
#             time.sleep(0.5)
#             print("...")
#             time.sleep(0.5)
#             print("...")
#             time.sleep(0.5)

#             filename = "Lista_biblioteca.json"

#             file = open(filename, "r", encoding='utf-8')
#             data = file.read()
#             data = json.loads(data)
#             data.append(salvar)

#             file = open(filename, 'w+', encoding='utf-8')
#             data = json.dumps(data)
#             file.write(data)
#             file.close()

#             print("Cadastro finalizado!")
#             time.sleep(2)
#             clear_console()
#             break


# def opcao2():
#     file = open(filename, "r", encoding='utf-8')
#     data = file.read()
#     data = json.loads(data)
#     i = 0
#     for nome in data:
        
#         print(i,"-",nome['nome_biblioteca'])
#         i+=1

#     ent_numero = int(input("Digite o numero da biblioteca para ser apagada: "))
#     data.pop(ent_numero)
#     file = open(filename, 'w+', encoding='utf-8')
#     data = json.dumps(data)
#     file.write(data)
#     file.close()

# def opcao3():
#     clear_console()
#     file = open(filename, "r", encoding='utf-8')
#     data = file.read()
#     data = json.loads(data)
#     i = 0
#     for nome in data:
        
#         print(i,"-","Nome: ",nome["nome_biblioteca"] )
#         print(" ","Telefone: ",nome["telefone"])
#         print(" ","Endereço: ",nome["endereço"])
#         print(" ","Entidade pública ou privada: ",nome["publica"])
#         print(" ","Gerente:",nome["gerente"])
#         print(" ","Tamanho do acervo:",nome["tamanho"])
#         print("-"*30)
        
#         i+=1
#     time.sleep(10)
    
# def opcao4():
#     file = open(filename, "r", encoding='utf-8')
#     data = file.read()
#     data = json.loads(data)
#     i = 0
#     print("Lista de Bibliotecas cadastradas no sistema:")
#     print("-"*30)
#     for nome in data:
        
#         print(i,"-","Nome: ",nome["nome_biblioteca"] )
#         print(" ","Telefone: ",nome["telefone"])
#         print(" ","Endereço: ",nome["endereço"])
#         print(" ","Entidade pública ou privada: ",nome["publica"])
#         print(" ","Gerente:",nome["gerente"])
#         print(" ","Tamanho do acervo:",nome["tamanho"])
#         print("-"*30)
#         i+=1
#     print("-"*30)
#     biblioteca = int(input("Digite o número da biblioteca a ser alterado: "))
#     data.pop(biblioteca)
#     file = open(filename, 'w+', encoding='utf-8')
#     data = json.dumps(data)
#     file.write(data)
#     file.close()
#     opcao1()

