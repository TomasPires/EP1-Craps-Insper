# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 18:13:40 2020

@author: tprfe
"""

#EP1-Craps Insper
#Produzido por Tomás Selaibe Pires e Daniel Parnes
#Design de Software - 2020.1


import random                  #Adicionando a biblioteca random para o sorteio do número dos dados


def dado1():                   #Definindo a função para o Dado 1
    a = random.randint(1,6)
    return a
def dado2():                   #Fazendo o mesmo para o Dado 2
    b = random.randint(1,6)
    return b

print("Bem vindo ao Craps Insper!") #Saudando o jogador
iniciar = input("Para começar o jogo basta digitar iniciar. ")   
iniciar = iniciar.upper()      #Transforma as letras da string em maiúsculas
if iniciar != 'INICIAR':
    print('Tenha um ótimo dia!')
else:                            #Aqui começa o jogo
    print('Iniciando o jogo...')
    
    