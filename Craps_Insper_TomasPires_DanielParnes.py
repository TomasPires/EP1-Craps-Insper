# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 18:13:40 2020

@author: tprfe
"""

#EP1-Craps Insper
#Produzido por Tomás Selaibe Pires e Daniel Parnes
#Design de Software - 2020.1


import random                  #Adicionando a biblioteca random para o sorteio do número dos dados



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

def pass_line(dado1, dado2):      #Pass Line Bet
    soma = dado1 + dado2
    ganhou = False
    point = False
    if (soma == 7) or (soma == 11):
        ganhou = True
    elif (soma == 2) or (soma == 3) or (soma == 12):
        ganhou = False
    else:
        point = True
    return ganhou, point, dado1, dado2

def field(dado1, dado2):          #Field Bet
    soma = dado1+dado2
    ganhou = False
    ganhou_dobro = False
    ganhou_triplo = False
    if (soma == 5) or (soma == 6) or (soma == 7) or (soma == 8):
        ganhou = False
    elif  (soma == 3) or (soma == 4) or (soma == 9) or (soma == 10) or (soma == 11):
        ganhou = True            #O jogador ganha o que apostou
    elif soma == 2:              #O jogador ganha o dobro do que apostou
        ganhou = True
        ganhou_dobro = True
    else:                        #O jogador ganha o triplo do que apostou
        ganhou = True
        ganhou_triplo = True
    return ganhou, ganhou_dobro, ganhou_triplo

def any_craps(dado1, dado2):     #Any Craps Bet
    soma = dado1+dado2
    ganhou = False
    if (soma == 2) or (soma == 3) or (soma == 12):
        ganhou = True
    else:
        ganhou = False
    return ganhou

def twelve(dado1, dado2):        #Any Craps Bet
    soma = dado1+dado2
    ganhou = False
    if soma == 12:
        ganhou = True
    else:
        ganhou = False
    return ganhou
        
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
            come_out = True                   #Run da fase come out
            point_run = False                 #Run da fase point
            print(regras_come_out())
            
            
            while come_out:                   #Loop da fase Come Out, que muda caso o jogador passe para Point na Pass Line Bet
                print("Você está na fase 'Come Out'")
                print("Fichas disponíveis: {0}".format(fichas))
                if fichas == 0:
                    come_out = False
                else:
                    jogar = input("Para sair do jogo digite 'sair'. Para continuar digite 'apostar'")
                    jogar = jogar.upper()
                    
                    if jogar == 'SAIR':
                        sair = input("Para encerrar o jogo digite 'sair' novamente. Caso deseje apenas recomeçar o jogo, digite 'recomeçar'" )
                        sair = sair.upper()
                        if sair == 'SAIR':
                            print('Até mais!')
                            come_out = False
                            run = False
                        elif sair == 'RECOMEÇAR':
                            print("Reiniciando...")
                            come_out = False                    
                    else:
                        dado1 = random.randint(1,6)
                        dado2 = random.randint(1,6)
                        tipo_aposta = input("Em qual tipo de aposta (Pass Line, Field, Any Craps, Twelve) você deseja apostar? ")
                        tipo_aposta = tipo_aposta.upper()
                        aposta = int(input("Quantas fichas você deseja apostar? "))
                        fichas-=aposta                   
                        
                        if tipo_aposta == 'PASS LINE':
                            if (pass_line(dado1, dado2)[0]) == True:      #Jogador ganhou a Pass Line Bet
                                print("Você ganhou {0] fichas!".format(aposta))
                                aposta+=aposta
                                fichas+=aposta                                
                            elif (pass_line(dado1, dado2)[0]) == False:
                                print("Você perdeu {0} fichas.".format(aposta))
                            elif (pass_line(dado1, dado2)[1]) == True:
                                print("Voce passou para a fase 'Point'")
                                come_out = False
                                point_run = True
                                
                        
                        elif tipo_aposta == 'FIELD':
                            if (field(dado1, dado2)[0]) == False:
                                print("Você perdeu tudo.")
                                come_out = False
                            elif (field(dado1, dado2)[0]) == True:
                                if (field(dado1, dado2)[1]) == True:
                                    aposta+=aposta*2
                                    fichas+=aposta
                                    print("Você ganhou {0] fichas!".format(2*aposta))
                                elif (field(dado1, dado2)[2]) == True:
                                    aposta+=aposta*3
                                    fichas+=aposta
                                    print("Você ganhou {0} fichas!".format(3*aposta))
                                else:
                                    print("Você ganhou {0} fichas!".format(aposta))
                                    aposta+=aposta
                                    fichas+=aposta                                    
                        
                        elif tipo_aposta == 'ANY CRAPS':
                            if any_craps(dado1, dado2) == True:
                                aposta+=aposta*7
                                fichas+=aposta
                                print("Você ganhou {0} fichas!".format(7*aposta))
                            else:
                                print("Você perdeu {0} fichas.".format(aposta))

                        elif tipo_aposta == 'TWELVE':
                            if twelve(dado1, dado2) == True:
                                print("Você ganhou {0} fichas!".format(30*aposta))
                                aposta+=30*aposta
                                fichas+=aposta
                            else:
                                print("Você perdeu {0} fichas.".format(aposta))

            print(regras_point())
            while point_run:
                if fichas == 0:
                    come_out = False
                else:
                    jogar = input("Para sair do jogo digite 'sair'. Para continuar digite 'apostar'")
                    jogar = jogar.upper()
                    
                    if jogar == 'SAIR':
                        sair = input("Para encerrar o jogo digite 'sair' novamente. Caso deseje apenas recomeçar o jogo, digite 'recomeçar'" )
                        sair = sair.upper()
                        if sair == 'SAIR':
                            print('Até mais!')
                            point_run = False
                            run = False
                        elif sair == 'RECOMEÇAR':
                            print("Reiniciando...")
                            point_run = False  
                            
                    else:
                        print("Você está na fase 'Point'")
                        print("Fichas disponíveis: {0}".format(fichas))
                                                
        























                        
