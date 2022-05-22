
import json
import time
import os

filename = "Lista_biblioteca.json"
def clear_console():
    os.system('cls')


def opcao3():
    clear_console()
    file = open(filename, "r", encoding='utf-8')
    data = file.read()
    data = json.loads(data)
    i = 0
    for nome in data:
        
        print(i,"-","Nome: ",nome["nome_biblioteca"] )
        print(" ","Telefone: ",nome["telefone"])
        print(" ","Endereço: ",nome["endereço"])
        print(" ","Entidade pública ou privada: ",nome["publica"])
        print(" ","Gerente:",nome["gerente"])
        print(" ","Tamanho do acervo:",nome["tamanho"])
        print("-"*30)
        
        i+=1
    time.sleep(10)