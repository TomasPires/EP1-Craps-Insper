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

def regras_come_out():         #Informações sobre a fase Come Out
    print("Você está na fase 'Come Out'.\nNessa fase você poderá apostar nas seguintes opções: Pass Line Bet, Field, Any Craps e Twelve." )
    print("Pass Line Bet: O jogador vence a rodada caso a soma dos dados lançados for 7 ou 11. Se os dados somarem 2, 3 ou 12, o jogador perde a rodada. Se a soma dos dados for diferente das anteriores, o jogo passa para a fase 'Point'.")
    print("Field: Nessa aposta, o jogador ganha o que apostou caso a soma dos dados for 3, 4, 9, 10 ou 11. Se a soma for 2, o jogador ganha o dobro que apostou e, se for 12, o jogador ganha o triplo.")
    print("Any Craps: Nessa aposta, se os dados somarem 2, 3 ou 12, o jogador ganha sete vezes o que apostou. Caso contrário, perde a aposta. ")
    print("Twelve: Nessa aposta, o jogador ganha trinta vezes o que apostou caso os dados somarem 12. Do contrário, perde a aposta.")

def regras_point():            #Informações sobre a fase Point
    print("Você está na fase 'Point'.\nNessa fase você poderá apostar nas seguintes opções: Pass Line Bet, Field, Any Craps e Twelve." )
    print("Field: Nessa aposta, o jogador ganha o que apostou caso a soma dos dados for 3, 4, 9, 10 ou 11. Se a soma for 2, o jogador ganha o dobro que apostou e, se for 12, o jogador ganha o triplo.")
    print("Any Craps: Nessa aposta, se os dados somarem 2, 3 ou 12, o jogador ganha sete vezes o que apostou. Caso contrário, perde a aposta. ")
    print("Twelve: Nessa aposta, o jogador ganha trinta vezes o que apostou caso os dados somarem 12. Do contrário, perde a aposta.")

def pass_line(dado1, dado2, valor_aposta):      #Pass Line Bet
    soma = dado1+dado2
    ganhou = False
    point = False
    if (soma == 7) or (soma == 11):
        ganhou = True
        return ganhou
    elif (soma == 2) or (soma == 3) or (soma == 12):
        ganhou = False
        return ganhou
    else:
        point = True
        return point

def field(dado1, dado2, valor_aposta):
    soma = dado1+dado2
    ganhou = False
    if soma 
        
print("Bem vindo ao Craps Insper! \nPara começar o jogo basta digitar iniciar. ") #Saudando o jogador
iniciar = input("Digite aqui: ")   
iniciar = iniciar.upper()      #Transforma as letras da string em maiúsculas
if iniciar != 'INICIAR':
    print('Tenha um ótimo dia!')
else:                                 
    run = True
    print('Iniciando o jogo...')     #Aqui começa o jogo
    while run:
        fichas = int(input("Comece por comprar uma quantidade de fichas. Quantas fichas você deseja comprar? "))
        if fichas <= 0:
            print("Você deve apostar um número de fichas maior que zero.")
        else:
            run_aposta = True
            while run_aposta:
                print(regras_come_out())
                tipo_aposta = input("Em qual tipo de aposta (Pass Line, Field, Any Craps, Twelve) você deseja apostar? ")
                tipo_aposta = tipo_aposta.upper()
                valor_aposta = int(input("Quantas fichas você deseja apostar? "))
                if tipo_aposta == 'PASS LINE':
                    
            
            
            
            
        
    
    