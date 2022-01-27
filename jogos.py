import forca
import advinhacao

def escolha_jogo():
    ###################### cabeçalho do codigo ###################################
    print('*********************************')
    print('*********Escolha o jogo**********')
    print('*********************************')

    print("(1) Forca\n(2) Advinhação")

    jogo = int(input("Qual jogo? "))

    if(jogo == 1):
        print("\n Jogando forca\n\n")
        forca.jogar()

    elif(jogo == 2):
        print("\n Jogando advinhação\n\n")
        advinhacao.jogar()

if(__name__ == "__main__"):
    escolha_jogo()