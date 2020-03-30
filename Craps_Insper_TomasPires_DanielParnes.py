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

print("Bem vindo ao Craps Insper! \nPara começar o jogo basta digitar iniciar. ") #Saudando o jogador
iniciar = input()   
iniciar = iniciar.upper()      #Transforma as letras da string em maiúsculas
if iniciar != 'INICIAR':
    print('Tenha um ótimo dia!')
else:                                 
    run = True
    print('Iniciando o jogo...')     #Aqui começa o jogo
    while run:
        fichas = int(input("Comece por comprar uma quantidade de fichas. Quantas fichas você deseja comprar? "))
        
    
    