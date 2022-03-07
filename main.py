import adivinhacao
import forca
import ppt


def main_menu():
    print('*********************************')
    print('Bem vindo ao menu de jogos!')
    print('*********************************')
    print('(1) Adivinhação (2) Forca (3) Pedra, Papel ou Tesoura (4) Sair')

    option = int(input('Insira a opção desejada: '))
    if(option == 1):
        adivinhacao.menu()
    elif(option == 2):
        forca.menu()
    elif(option == 3):
        ppt.menu()
    else:
        quit()

if(__name__ == '__main__'):
    main_menu()