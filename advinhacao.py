def jogar():
    #--------------------- Bibliotecas importadas -----------------------------#
    import random
    #--------------------- cabeçalho do codigo --------------------------------#
    print('*********************************')
    print('bem vindo ao jogo de adivinhação!')
    print('*********************************')

    #-------------------- variáveis de scopo geral ----------------------------#
    numero_secreto = random.randrange(1, 101)
    total_tentativas = 0

    jogador = input('Qual seu nome? ')

    #-------------------- definindo a dificuldade --------------------------------#
    print('{}, estas são as dificuldades disponiveis: \n (1) Facil \n (2) Médio \n (3) Difícil\n'.format(jogador))
    dificuldade = int(input('Defina a dificuldade: '))

    if(dificuldade == 1):
        print('Você escolheu a dificuldade fácil!')
        total_tentativas = 20
    elif(dificuldade == 2):
        print('Você escolheu a dificuldade médio!')
        total_tentativas = 10
    else:
        print('Você escolheu a dificuldade difícil!')
        total_tentativas = 5

    #------------------------------ LOOP -----------------------------------------#
    for rodada in range(1, total_tentativas + 1):
        print("tentativa {} de {}".format(rodada, total_tentativas))
        chute = int(input("Digite um numero de 1 a 100: "))
        print("você digitou", chute)

        if(chute < 1 or chute > 100):
            print("Você deve digitar um numero entre 1 e 100")
            continue
        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if(acertou):
            print("Parabens {} você acertou na {}ª tentativa!" .format(jogador, rodada))
            break
        else:
            if(maior):
                print("você errou! O seu chute foi maior que o numero secreto")
            elif(menor):
                print("você errou! O seu chute foi menor que o numero secreto")

    print("Fim do jogo, o numero secreto era: {}!".format(numero_secreto))
if(__name__ == "__main__"):
    jogar()
