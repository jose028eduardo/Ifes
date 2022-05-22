import time
import os
import json
def clear_console():
    os.system('cls')

filename = "Lista_biblioteca.json"
def opcao2():
    file = open(filename, "r", encoding='utf-8')
    data = file.read()
    data = json.loads(data)
    i = 0
    for nome in data:
        
        print(i,"-",nome['nome_biblioteca'])
        i+=1

    ent_numero = int(input("Digite o numero da biblioteca para ser apagada: "))
    data.pop(ent_numero)
    file = open(filename, 'w+', encoding='utf-8')
    data = json.dumps(data)
    file.write(data)
    file.close()