# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 18:13:40 2020

@author: tprfe
"""

#EP1-Craps Insper
#Produzido por Tomás Selaibe Pires
#Design de Software - 2020.1


import random                  #Adicionando a biblioteca random para o sorteio do número dos dados


def regras_come_out():         #Informações sobre a fase Come Out
    return("Você está na fase 'Come Out'.\nNessa fase você poderá apostar nas seguintes opções: Pass Line Bet, Field, Any Craps e Twelve. \nPass Line Bet: O jogador vence a rodada caso a soma dos dados lançados for 7 ou 11. Se os dados somarem 2, 3 ou 12, o jogador perde a rodada. Se a soma dos dados for diferente das anteriores, o jogo passa para a fase 'Point'.\nField: Nessa aposta, o jogador ganha o que apostou caso a soma dos dados for 3, 4, 9, 10 ou 11. Se a soma for 2, o jogador ganha o dobro que apostou e, se for 12, o jogador ganha o triplo.\nAny Craps: Nessa aposta, se os dados somarem 2, 3 ou 12, o jogador ganha sete vezes o que apostou. Caso contrário, perde a aposta. \nTwelve: Nessa aposta, o jogador ganha trinta vezes o que apostou caso os dados somarem 12. Do contrário, perde a aposta.")

def regras_point():            #Informações sobre a fase Point (as mesmas da outra fase, com exceção da Pass Line Bet, que é substituída pelo Point)
    return("Nessa fase você poderá apostar nas seguintes opções: Field, Any Craps e Twelve, além de ganhar se os dados somarem o valor do Point\nPoint: O valor tirado na fase anterior em 'Pass Line Bet', caso haja um, passa ser o 'Point'. o Lançamento dos dados deve ser igual ao do Point. Se anova soma dos dados é a mesma do que foi guardado no Point, o jogador ganha o mesmo valor que apostou. Se sair uma soma de valor 7 o jogador perde tudo. Caso saia qualquer outro número, se mantem na fase de 'Point'.\nField: Nessa aposta, o jogador ganha o que apostou caso a soma dos dados for 3, 4, 9, 10 ou 11. Se a soma for 2, o jogador ganha o dobro que apostou e, se for 12, o jogador ganha o triplo.\nAny Craps: Nessa aposta, se os dados somarem 2, 3 ou 12, o jogador ganha sete vezes o que apostou. Caso contrário, perde a aposta. \nTwelve: Nessa aposta, o jogador ganha trinta vezes o que apostou caso os dados somarem 12. Do contrário, perde a aposta.")

def pass_line(dado1, dado2):      #Pass Line Bet
    soma = dado1 + dado2
    ganhou = False
    if (soma == 7) or (soma == 11):
        ganhou = True
    elif (soma == 2) or (soma == 3) or (soma == 12):
        ganhou = False
    return ganhou

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
        
print("Bem vindo ao Craps Insper! \nPara começar o jogo basta digitar 'iniciar'. ") #Saudando o jogador
iniciar = input("Digite aqui: ")   
iniciar = iniciar.upper()      #Transforma as letras da string em maiúsculas
if iniciar != 'INICIAR':
    print('Tenha um ótimo dia!')
else:                                 
    run = True
    print('Iniciando o jogo...\n')     #Aqui começa o jogo
    
    
    while run:
        fichas = 100
        come_out = True                   #Run da fase come out
        point_run = False                 #Run da fase point
        print(regras_come_out())
        
        while come_out:                   #Loop da fase Come Out, que muda caso o jogador passe para Point na Pass Line Bet
            if fichas <= 0:
                print("Você não tem mais fichas disponíveis")
                come_out = False
                run = False
            else:
                print("Fase atual: Come Out")
                print("Fichas disponíveis: {0}".format(fichas))
                jogar = input("Para sair do jogo digite 'sair'. Para continuar digite 'apostar': ")
                jogar = jogar.upper()
                
                if jogar == 'SAIR':
                    sair = input("Para encerrar o jogo digite 'sair' novamente. Caso deseje apenas recomeçar o jogo, digite 'recomeçar': " )
                    sair = sair.upper()
                    if sair == 'SAIR':
                        print('Até mais!')
                        come_out = False
                        run = False
                    elif sair == 'RECOMEÇAR':                 #Retorna para o início do código, fora do loop come_out
                        print("Reiniciando...")
                        come_out = False                    
                else:
                    dado1 = 6
                    dado2 = 2
                    tipo_aposta = input("Em qual tipo de aposta (Pass Line, Field, Any Craps, Twelve) você deseja apostar? ")
                    tipo_aposta = tipo_aposta.upper()
                    aposta = int(input("Quantas fichas você deseja apostar? "))
                    apostas = []
                    apostas.append(tipo_aposta)
                    apostando = True
                    mesa = 0                              #fichas apostadas pelo jogador
                    mesa+=aposta
                    while apostando:
                        if mesa>fichas:
                            print("Você não pode apostar mais fichas do que possui. Recomece as apostas")
                            print("Reiniciando...\n")
                            break
                        else:
                            tipo_aposta = input("Gostaria de fazer mais apostas? ")
                            tipo_aposta = tipo_aposta.upper()
                            if tipo_aposta == 'SIM':
                                tipo_aposta = input("Em qual tipo de aposta (Pass Line, Field, Any Craps, Twelve) você deseja apostar? ")
                                tipo_aposta = tipo_aposta.upper()
                                aposta = int(input("Quantas fichas você deseja apostar? "))
                                apostas.append(tipo_aposta)
                                mesa+=aposta
                            
                            else:
                                apostando = False
                                print("Os dados somaram: ", dado1+dado2)
                n_aposta = 0
                pass_valor = 0               #Introduzindo variaveis para guardar os valores ganhos por cada aposta para não interferir nas demais
                field_valor = 0              #Estes serão somados ao montante de fichas no final
                any_valor = 0
                twelve_valor = 0
                while n_aposta<len(apostas) and (mesa<fichas):
                    if apostas[n_aposta] == 'PASS LINE':
                        print("Apostando em 'Pass Line Bet'")
                        if (pass_line(dado1, dado2)) == True:      #Jogador ganhou a Pass Line Bet
                            print("Você ganhou {0] fichas!".format(aposta))
                            pass_valor = aposta
                            n_aposta+=1
                        elif (dado1+dado2) == 4 or (dado1+dado2) == 5 or (dado1+dado2) == 6 or (dado1+dado2) == 8 or (dado1+dado2) == 9 or (dado1+dado2) == 10:
                            print("Voce passou para a fase 'Point'")
                            point = dado1+dado2               #Estabelecendo o valor de Point
                            aposta_point = aposta
                            come_out = False
                            point_run = True
                            break    
                            
                        else:
                            pass_valor-=aposta
                            print("Você perdeu {0} fichas.".format(aposta))
                            n_aposta+=1

                            
                    
                    elif apostas[n_aposta] == 'FIELD':
                        print("Apostando em 'Field Bet'")
                        if (field(dado1, dado2)[0]) == False:
                            print("Você perdeu tudo.")
                            fichas = 0
                            break                             
                        elif (field(dado1, dado2)[0]) == True:
                            if (field(dado1, dado2)[1]) == True:
                                field_valor+=aposta*2
                                n_aposta+=1
                                print("Você ganhou {0] fichas!".format(2*aposta))
                            elif (field(dado1, dado2)[2]) == True:
                                field_valor+=aposta*3
                                print("Você ganhou {0} fichas!".format(3*aposta))
                                n_aposta+=1
                            else:
                                print("Você ganhou {0} fichas!".format(aposta))
                                field_valor+=aposta
                                n_aposta+=1
                    
                    elif apostas[n_aposta] == 'ANY CRAPS':
                        print("Apostando em 'Any Craps'")
                        if any_craps(dado1, dado2) == True:
                            any_valor+=aposta*7
                            print("Você ganhou {0} fichas!".format(7*aposta))
                            n_aposta+=1
                        else:
                            any_valor-=aposta
                            print("Você perdeu {0} fichas.".format(aposta))
                            n_aposta+=1

                    elif apostas[n_aposta] == 'TWELVE':
                        print("Apostando em 'Twelve'")
                        if twelve(dado1, dado2) == True:
                            print("Você ganhou {0} fichas!".format(30*aposta))
                            twelve_valor+=aposta*30
                            n_aposta+=1
                        else:
                            twelve_valor-=aposta
                            print("Você perdeu {0} fichas.".format(aposta))
                            n_aposta+=1
            fichas+=pass_valor + field_valor + any_valor + twelve_valor   

            while point_run:
                if fichas <= 0:
                    print("Você não tem mais fichas disponíveis")
                    point_run = False
                    come_out = False
                    run = False
                else:
                    print("Fase atual: 'Point'")
                    print("Fichas disponíveis: {0}".format(fichas))
                    jogar = input("Para sair do jogo digite 'sair'. Para continuar digite 'apostar': ")
                    jogar = jogar.upper() 
                    if jogar == 'SAIR':
                        sair = input("Para encerrar o jogo digite 'sair' novamente. Caso deseje apenas recomeçar o jogo, digite 'recomeçar': " )
                        sair = sair.upper()
                        if sair == 'SAIR':
                            print('Até mais!')
                            point_run = False
                            come_out = False
                            run = False
                        elif sair == 'RECOMEÇAR':                 #Retorna para o início do código, fora do loop come_out
                            print("Reiniciando...")
                            point_run = False
                            come_out = False
                    else:
                        dado1 = 6
                        dado2 = 2
                        tipo_aposta = input("Em qual tipo de aposta (Field, Any Craps, Twelve) você deseja apostar? ")
                        tipo_aposta = tipo_aposta.upper()
                        aposta = int(input("Quantas fichas você deseja apostar? "))
                        apostas = []
                        apostas.append(tipo_aposta)
                        apostando = True
                        mesa = 0 
                        mesa+=aposta
                        while apostando:
                            tipo_aposta = input("Gostaria de fazer mais apostas? ")
                            tipo_aposta = tipo_aposta.upper()
                            if tipo_aposta == 'SIM':
                                tipo_aposta = input("Em qual tipo de aposta (Field, Any Craps, Twelve) você deseja apostar? ")
                                tipo_aposta = tipo_aposta.upper()
                                aposta = int(input("Quantas fichas você deseja apostar? "))
                                apostas.append(tipo_aposta)
                            if mesa>fichas:
                                print("Você não pode apostar mais fichas do que possui. Por favor, refaça a última aposta")
                                break
                            else:
                                apostando = False
                        print("Os dados somaram: ", dado1+dado2)
                        n_aposta = 0
                        point_valor = pass_valor
                        while n_aposta<len(apostas):
                            if (dado1+dado2) == point:
                                print("Você ganhou o Point")
                                fichas+=aposta_point
                                point_run = False
                                break
                            elif (dado1+dado2) == 7:
                                print("Você perdeu tudo")
                                fichas = 0
                                break
                            
                            elif apostas[n_aposta] == 'FIELD':
                                print("Apostando em 'Field Bet'")
                                if (field(dado1, dado2)[0]) == False:
                                    print("Você perdeu tudo.")
                                    fichas = 0
                                    break                             
                                elif (field(dado1, dado2)[0]) == True:
                                    if (field(dado1, dado2)[1]) == True:
                                        field_valor+=aposta*2
                                        n_aposta+=1
                                        print("Você ganhou {0] fichas!".format(2*aposta))
                                    elif (field(dado1, dado2)[2]) == True:
                                        field_valor+=aposta*3
                                        print("Você ganhou {0} fichas!".format(3*aposta))
                                        n_aposta+=1
                                    else:
                                        print("Você ganhou {0} fichas!".format(aposta))
                                        field_valor+=aposta
                                        n_aposta+=1
                            
                            elif apostas[n_aposta] == 'ANY CRAPS':
                                print("Apostando em 'Any Craps'")
                                if any_craps(dado1, dado2) == True:
                                    any_valor+=aposta*7
                                    print("Você ganhou {0} fichas!".format(7*aposta))
                                    n_aposta+=1
                                else:
                                    any_valor-=aposta
                                    print("Você perdeu {0} fichas.".format(aposta))
                                    n_aposta+=1
        
                            elif apostas[n_aposta] == 'TWELVE':
                                print("Apostando em 'Twelve'")
                                if twelve(dado1, dado2) == True:
                                    print("Você ganhou {0} fichas!".format(30*aposta))
                                    twelve_valor+=aposta*30
                                    n_aposta+=1
                                else:
                                    twelve_valor-=aposta
                                    print("Você perdeu {0} fichas.".format(aposta))
                                    n_aposta+=1
                    fichas+=pass_valor + field_valor + any_valor + twelve_valor
                    
if fichas == 0:                     #O programa antes estava imprimindo "Até mais!" duas vezes
    print("Até mais!")

            
        





















                        
