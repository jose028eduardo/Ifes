import opcao1
import json
import os

filename = "Lista_biblioteca.json"
def clear_console():
    os.system('cls')

def opcao4():
    file = open(filename, "r", encoding='utf-8')
    data = file.read()
    data = json.loads(data)
    i = 0
    print("Lista de Bibliotecas cadastradas no sistema:")
    print("-"*30)
    for nome in data:
        
        print(i,"-","Nome: ",nome["nome_biblioteca"] )
        print(" ","Telefone: ",nome["telefone"])
        print(" ","Endereço: ",nome["endereço"])
        print(" ","Entidade pública ou privada: ",nome["publica"])
        print(" ","Gerente:",nome["gerente"])
        print(" ","Tamanho do acervo:",nome["tamanho"])
        print("-"*30)
        i+=1
    print("-"*30)
    biblioteca = int(input("Digite o número da biblioteca a ser alterado: "))
    data.pop(biblioteca)
    file = open(filename, 'w+', encoding='utf-8')
    data = json.dumps(data)
    file.write(data)
    file.close()
    opcao1.escolha1()