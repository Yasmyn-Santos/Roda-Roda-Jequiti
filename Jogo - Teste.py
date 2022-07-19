import random


sim = "s"
x = "s"

jogador1,jogador2,jogador3 = "Ana","Barbara","Carlos"

roleta = [100,150,200,250,300,350,400,450,500,550,600,650,700,750,800,850,900,950,1000,1000,"PASSA A VEZ","PASSA A VEZ","PERDE TUDO","PERDE TUDO"]

rodada = 1
turno = 1

ponto_player1=0
ponto_player2=0
ponto_player3=0

jogadores = [jogador1,jogador2,jogador3]

pontuacao = [ponto_player1,ponto_player2,ponto_player3]

indice = 0

while x == sim:
        baseDados= {'Nome': ['pedro', 'paulo', 'jose', 'henrique', 'daniel', 'marcelo', 'antonio', 'claudio', 'alexandre', 'bruna', 'luisa', 'simone', 'eliana'],
                    'Carro': ['fusca', 'uno', 'gol', 'siena', 'argo', 'celta', 'fox', 'voyage', 'corolla', 'onix'],
                    'País':['albania', 'argentina', 'catar', 'bahamas', 'colombia', 'franca', 'alemanha', 'italia', 'brasil']}

        tema = random.choice(list(baseDados.keys()))
        valor_roleta = random.choice(roleta)

        pala1, pala2, pala3 = random.sample(baseDados[tema], k=3)

        letras_escolhidas = []

        lacunas1 = ["_"] * len(pala1)
        lacunas2 = ["_"] * len(pala2)
        lacunas3 = ["_"] * len(pala3)

        print ("\nBem vindo ao jogo Roda Roda Jequiti!!!")
        print ("O objetivo é tentar acertar a palavra escondida")
        print ("O jogador terá que tentar uma letra por vez")
        print ("Deverá escolher uma letra qualquer de três palavras \nque pertençam a um tema específico")
        print ("Caso você acerte, a letra será inserida no espaço em branco \npara que você chegue mais perto de acerta-la")
        print ("Caso você erre, você passará a vez")

        input('\nDigite qualquer letra para começar: ')

        print("\nVez de:{}".format(jogador1))
        print("\n+================================================")

        if valor_roleta != "PASSA A VEZ" and valor_roleta != "PERDE TUDO":
                print("\nValendo:R${}".format(valor_roleta))

        print ("\nTema:{}\n".format(tema))        
                        
                                
        print (lacunas1)
        print (lacunas2)
        print (lacunas3)
        print("\n+================================================")


        #Roda roleta

        while ''.join(lacunas1) != pala1 or ''.join(lacunas2) != pala2 or ''.join(lacunas3) != pala3:
                if valor_roleta != "PASSA A VEZ" and valor_roleta != "PERDE TUDO":

                        letra = input("\n\nQual letra você quer tentar? ")

                        while letra in letras_escolhidas:
                                print ("\nEssa letra já foi escolhida, tente outra")
                                letra = input("\nQual letra você quer tentar? ")
                        letras_escolhidas.append(letra)
                        if letra in pala1 or letra in pala2 or letra in pala3:
                                print ("\n\nParabéns, você acertou a letra!")
                                for j in range(len(pala1)):
                                        if letra == pala1[j]:
                                                lacunas1[j] = letra.upper()
                                for l in range(len(pala2)):
                                        if letra == pala2[l]:
                                                lacunas2[l] = letra.upper()
                                for m in range(len(pala3)):
                                        if letra == pala3[m]:
                                                lacunas3[m] = letra.upper()
                                pontuacao[indice]=pontuacao[indice]+valor_roleta

                        else:
                                print ("\n\nQue pena, você errou!\nPASSOU A VEZ!\nProximo jogador!" )
                                if indice > 2:
                                        indice=0
                                else:
                                        indice=(indice+1)%3
                                        
                        valor_roleta = random.choice(roleta)

                        # Como estão as lacunas da palavra
                        print("+================================================")
                        print("|RODADA: {} - TURNO: {} ".format(rodada,turno))
                        print("+================================================")
                        print("|ANA - {} | BARBARA - {} | CARLOS - {}".format(ponto_player1,ponto_player2,ponto_player3))
                        print("+================================================")
                        print("Vez do jogador: {}\nPontuação atual: {}\nPonto da roleta: \nPontuação atualizada: ".format(jogadores[indice%3],pontuacao[indice]))
                        print ("+================================================")
                        print("\nValendo:R${}".format(valor_roleta))

                        print ("\nTema:{}".format(tema))        
                        
                                
                        print (lacunas1)
                        print (lacunas2)
                        print (lacunas3)

                        # quais as letras ele já tentou
                        print ("\nAs letras já usadas:")
                        for item in letras_escolhidas:
                                print (item, end=" ")
                        print("\n+================================================")
                        turno = turno + 1
                elif valor_roleta != "PERDE TUDO" and valor_roleta == "PASSA A VEZ":
                        print ("\n\nQue pena, você errou!\nPASSOU A VEZ!\nProximo jogador!" )
                        if indice <= 2:
                                indice=0
                        else:
                                indice=(indice+1)%3
                                
                        valor_roleta = random.choice(roleta)
                        
                elif valor_roleta == "PERDE TUDO" and valor_roleta != "PASSA A VEZ":
                        print("{}, poxa você perdeu tudo :( ".format(jogadores[indice]))
                        pontuacao[indice]=pontuacao[indice]-pontuacao[indice]

                        valor_roleta = random.choice(roleta)

                        if indice <= 2:
                                indice=0
                        else:
                                indice=(indice+1)%3  
                                
                
        print ("\n\nPARABÉNS, VOCÊ VENCEU\n")
        print ("A palavra era", pala1 )
        print ("A palavra era", pala2 )
        print ("A palavra era", pala3 )
        rodada = rodada+1
        x = ""
        x = str(input("\nDeseja continuar? (s)sim/(n)não:"))
        
        
        opaaa
        



        




