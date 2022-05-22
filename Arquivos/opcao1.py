import time
import os
import json

def clear_console():
    os.system('cls')

filename = "Lista_biblioteca.json"

def escolha1():
    nome_biblioteca = input("Digite o nome da Biblioteca: ")
    telefone = input("Digite o telefone da Biblioteca: ")
    endereço = input("Digite o endereço: ")
    publica = input("Diga se esta biblioteca é particular ou pública: ")
    gerente = input("Digite o nome do(a) gerente: ")
    tamanho = input("Digite o tamanho do acervo da biblioteca: ")
    
    clear_console()

    
    print("-"*30)
    salvar = ({"nome_biblioteca": (nome_biblioteca), "telefone": (telefone), "publica": (
        publica), "endereço": (endereço), "gerente": (gerente), "tamanho": (tamanho)})

    

    print("Nome: ",salvar["nome_biblioteca"] )
    print("Telefone: ",salvar["telefone"])
    print("Endereço: ",salvar["endereço"])
    print("Entidade pública ou privada: ",salvar["publica"])
    print("Gerente:",salvar["gerente"])
    print("Tamanho do acervo:",salvar["tamanho"])
    print("-"*30)

    print("O cadastramento está correto? Responda com S ou N.")
    confirmaçao = input("Resposta: ")
    while True:
        if confirmaçao != "s" and confirmaçao != "S":

            escolha1()
        else:
            clear_console()
            print("-"*30)
            print("Finalizando cadastro...")
            time.sleep(0.5)
            print("...")
            time.sleep(0.5)
            print("...")
            time.sleep(0.5)

            

            file = open(filename, "r", encoding='utf-8')
            data = file.read()
            data = json.loads(data)
            data.append(salvar)

            file = open(filename, 'w+', encoding='utf-8')
            data = json.dumps(data)
            file.write(data)
            file.close()

            print("Cadastro finalizado!")
            time.sleep(2)
            clear_console()
            break

