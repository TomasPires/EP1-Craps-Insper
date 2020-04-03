# EP1-Craps-Insper
Exercício Problema 1

Produzido por Tomás Selaibe Pires Turma C - 1ºSemestre

O programa presente nesse repositório (Craps_Insper_TomásPires.py) se trata de um jogo de dados denominado Craps

O cógigo está estruturado em: 1- Definição das funções das apostas; 2-Comandos para começar o jogo; 3- Loop da fase Come Out; 4-Loop da fase Point

Há comentarios ao longo do código para explicar o significado de algumas funções.

Neste jogo, o jogador começa com 100 fichas e deve apostar em rodadas consecutivas em 4 tipos de apostas: Pass Line Bet, Field Bet, Any Craps e Twelve Bet
Em cada aposta, a soma dos dados é que determina se o jogador ganha ou perde as fichas apostadas
Abaixo seguem as regras exibidas ao jogador em cada rodada:

Você está na fase 'Come Out'. Nessa fase você poderá apostar nas seguintes opções: Pass Line Bet, Field, Any Craps e Twelve. Pass Line Bet: O jogador vence a rodada caso a soma dos dados lançados for 7 ou 11. Se os dados somarem 2, 3 ou 12, o jogador perde a rodada. Se a soma dos dados for diferente das anteriores, o jogo passa para a fase 'Point'.Field: Nessa aposta, o jogador ganha o que apostou caso a soma dos dados for 3, 4, 9, 10 ou 11. Se a soma for 2, o jogador ganha o dobro que apostou e, se for 12, o jogador ganha o triplo.Any Craps: Nessa aposta, se os dados somarem 2, 3 ou 12, o jogador ganha sete vezes o que apostou. Caso contrário, perde a aposta. Twelve: Nessa aposta, o jogador ganha trinta vezes o que apostou caso os dados somarem 12. Do contrário, perde a aposta.

Nessa fase você poderá apostar nas seguintes opções: Field, Any Craps e Twelve, além de ganhar se os dados somarem o valor do Point. Point: O valor tirado na fase anterior em 'Pass Line Bet', caso haja um, passa ser o 'Point'. o Lançamento dos dados deve ser igual ao do Point. Se anova soma dos dados é a mesma do que foi guardado no Point, o jogador ganha o mesmo valor que apostou. Se sair uma soma de valor 7 o jogador perde tudo. Caso saia qualquer outro número, se mantem na fase de 'Point'.Field: Nessa aposta, o jogador ganha o que apostou caso a soma dos dados for 3, 4, 9, 10 ou 11. Se a soma for 2, o jogador ganha o dobro que apostou e, se for 12, o jogador ganha o triplo.Any Craps: Nessa aposta, se os dados somarem 2, 3 ou 12, o jogador ganha sete vezes o que apostou. Caso contrário, perde a aposta. Twelve: Nessa aposta, o jogador ganha trinta vezes o que apostou caso os dados somarem 12. Do contrário, perde a aposta.

Em resumo, o jogador deve apostar em cada tipo de aposta o número de fichas especificado por ele. Conforme o resultado dos dados ele ganha ou perde a rodada, perdendo o número de fichas apostadas ou mais, dependendo da rodada.
