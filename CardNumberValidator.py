
##############################################
#            Card Number Validator           #
#              Coded By alikhandkk81         #       
#                01/13/018                   #
##############################################

 
import platform
import time
import os

so = platform.system()

def limpar():
    if  so == 'Windows':
	    os.system("cls")
    else:
	    os.system("clear")

cartoesValidos = []
cartoesInvalidos = []
todosCartoes = []

def novesFora(numero):
    resultado = 0
    numero = list(str(numero))
    for i in numero:
        resultado = resultado + int(i)
    return resultado

def impar(card):
    total = 0
    card = card[::2]
    for i in card:
        i = int(i)*2
        total = total + novesFora(i)
    return total

def par(card):
    total = 0
    card = list(card)
    card.pop(0)
    card = card[::2]
    for i in card:
        total = total + int(i)
    return total

def impar15(card):
    total = 0
    card = card[::2]
    for i in card:
        total = total + int(i)
    return total

def par15(card):
    total = 0
    card = list(card)
    total = total + novesFora(int(card[0])*2)
    card.pop(0)
    card = "".join(card)
    card = str(card)
    for i in card:
        i = int(i)*2
        total = total + novesFora(i)
    return total

def testar(numero):
    total = 0
    numero = str(numero)
    resultado = None
    quantidadeDeAlgarismos = len(numero)
    if quantidadeDeAlgarismos < 13 or quantidadeDeAlgarismos > 16:
        return "Invalid!"
    elif quantidadeDeAlgarismos == 15:
        total = par15(numero) + impar15(numero)
    else:
        total = par(numero) + impar(numero)
    if total % 10 == 0:
        resultado = "Valid!"
    else:
        resultado = "Invalid!"
    return resultado

def pegarNumerosDoArquivo(arquivo):
    arquivo = open(arquivo, "r")
    numeros = arquivo.readlines()
    lista = []
    for i in numeros:
        lista.append(i.replace('\n', ''))
    arquivo.close()
    return lista

def salvarTodos(cartoesValidos, cartoesInvalidos):
    #Cria arquivo e adiciona os cartoes validos.
    arquivo = open("AllCards.txt", 'w')
    arquivo.write("#######Valid Cards#######\n\n")
    arquivo.close()
    arquivo = open("AllCards.txt", 'a')
    for cartao in cartoesValidos:
        arquivo.write(cartao+"\n")
    arquivo.close()
    #Abre arquivo e adiciona os cartoes invalidos
    arquivo = open("AllCards.txt", 'a')
    arquivo.write("\n#######Invalid Cards#######\n\n")
    arquivo.close()
    arquivo = open("AllCards.txt", 'a')
    for cartao in cartoesInvalidos:
        arquivo.write(cartao+"\n")
    arquivo.close()

def salvarValidos(cartoesValidos):
    arquivo = open("ValidCardis.txt", 'w')
    for cartao in cartoesValidos:
        arquivo.write(str(cartao)+"\n")
    arquivo.close()

def salvarInvalidos(cartoesInvalidos):
    arquivo = open("InvalidCards.txt", 'w')
    for cartao in cartoesInvalidos:
        arquivo.write(str(cartao)+"\n")
    arquivo.close()

limpar()

op = int(input('''
                         ________________________
                        |                  ####  |
                        |                  VISA  |
                        | ####             ####  |
                        | ####                   |
                        |                        | 
                        |C4RD NUM8 B3RV 4L1D 4T0R|
                        |By   alikhandkk81       |      
                        |________________________|



                        [!] BY TEXT FILE  -----> 1
                        [!] BY NUMBER     -----> 2

>>> '''))
try:
    if op == 1:
        arquivo = input("\nTYPE THE FILE NAME\n\n>>> ")
        cartoes = pegarNumerosDoArquivo(arquivo)
        for cartao in cartoes:
            resultado = testar(cartao)
            time.sleep(0.1)
            print(cartao+" -----> "+resultado)
            todosCartoes.append(cartao)
            if resultado == "Valid!":
                cartoesValidos.append(cartao)
            else:
                cartoesInvalidos.append(cartao)

        opSalvar = int(input('''
        
        
        [!] SAVE ONLY INVALID CARD NUMBERS         -----> 1
        [!] SAVE ONLY VALID CARD NUMBERS           -----> 2
        [!] SAVE ALL CARD NUMBERS                  -----> 3
        [!] ALL OPTIONS (RECOMENDED)               -----> 4  
        
>>> '''))
        if opSalvar == 1:
            salvarInvalidos(cartoesInvalidos)
        elif opSalvar == 2:
            salvarValidos(cartoesValidos)
        elif opSalvar == 3:
            salvarTodos(cartoesValidos, cartoesInvalidos)
        else:
            salvarInvalidos(cartoesInvalidos)
            salvarValidos(cartoesValidos)
            salvarTodos(cartoesValidos, cartoesInvalidos)
        print("Saved!")
    
    if op == 2:
        cartao = input("\n\nTYPE A CARD NUMBER\n\n>>> ")
        print("\n\n"+cartao+" -----> "+testar(cartao)+"\n\n")
    
except:
    print("\n\nERROR! TRY AGAIN OR CONTACT THE DEVELOPER\n\n")
