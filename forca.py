import random
import main


def menu():
    print('*********************************')
    print('Bem vindo ao jogo de Forca!')
    print('*********************************')

    options_menu()


def read_rules():
    print('************************')
    print('Regras do jogo de Forca.')
    print('************************')
    print('(1) Você deve adivinhar a palavra.')
    print('(2) Você deve inserir somente uma única letra por vez.')
    print('(3) Seus erros te colocam mais perto da forca!')
    print('(4) Divirta-se!')

    options_not_menu()


def play():

    secret_word = generate_secret_word()
    right_letters = ['_' for i in secret_word]
    print(right_letters)

    attempts = 0
    acertou = False
    enforcou = False

    while(not acertou and not enforcou):
        guess = str(input('Chute uma letra: ')).strip().upper()

        if(guess in secret_word):
            index = 0
            for i in secret_word:
                if(guess == i):
                    right_letters[index] = i
                index += 1
        else:
            attempts += 1
            desenha_forca(attempts)
        print(right_letters)

        acertou = '_' not in right_letters
        enforcou = attempts == 7

    if(enforcou):
        imprime_mensagem_perdedor(secret_word)
    if(acertou):
        imprime_mensagem_vencedor()
    options_not_menu()


def options_not_menu():
    print('Opções disponíveis: (1) Jogar (2) Regras (3) Menu (4) Sair')
    option = int(input('Insira a opção desejada: '))
    try:
        options = {1: play, 2: read_rules, 3: menu, 4: quit}
        options[option]()
    except KeyError:
        print('Valor inválido!')
        options_not_menu()


def options_menu():
    print('(1) Jogar (2) Regras (3) Menu de jogos (4) Sair')
    option = int(input('Insira a opção desejada: '))
    try:
        options = {1: play, 2: read_rules, 3: main.main_menu, 4: quit}
        options[option]()
    except KeyError:
        print('Valor inválido!')
        options_menu()


def generate_secret_word():
    with open('palavras.txt') as file:
        words = [i.strip().upper() for i in file]

    number = random.randrange(0, len(words))
    secret_word = words[number]
    return secret_word


def imprime_mensagem_perdedor(secret_word):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(secret_word))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def desenha_forca(attempts):
    print("  _______     ")
    print(" |/      |    ")

    if(attempts == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(attempts == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(attempts == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(attempts == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(attempts == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(attempts == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (attempts == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


if (__name__ == '__main__'):
    menu()
