import random
import main


def menu():
    print('*********************************')
    print('Bem vindo ao jogo de adivinhação!')
    print('*********************************')

    options_menu()


def read_rules():
    print('******************************')
    print('Regras do jogo de adivinhação.')
    print('******************************')
    print('(1) Você deve adivinhar o número pensado pelo computador.')
    print('(2) Você deve inserir um número entre 1 e 100.')
    print('(3) O nível de dificuldade escolhido altera a quantidade de tentativas disponíveis.')
    print('(4) Divirta-se!')

    options_not_menu()


def play():
    secret_number = random.randrange(1, 101)
    attempts = choose_level()
    points = 1000

    for i in range(1, attempts + 1):
        print(f'Tentativa {i} de {attempts}.')
        guess = int(input('Digite seu chute: '))
        print(f'Você digitou o número {guess}.')

        if (guess < 1 or guess > 100):
            print('Você deve digitar um número entre 1 e 100.')
            continue

        right = guess == secret_number
        higher = guess > secret_number
        lower = guess < secret_number

        if (right):
            print('Você acertou!')
            print(f'Você fez {points} pontos.')
            break
        elif (higher):
            print('Você errou! O chute é maior que o número secreto.')
        elif (lower):
            print('Você errou! O chute é menor que o número secreto.')

        lost_points = abs(secret_number - guess)
        points -= lost_points

        if(attempts == i):
            print(f'O número pensado foi o {secret_number}.')

    print('Fim de jogo.')
    options_not_menu()


def choose_level():
    print('Níveis de dificuldade: (1) Fácil (2) Médio (3) Difícil')
    level = int(input('Insira o nível desejado: '))
    levels = {1 : 20, 2 : 10, 3 : 5}
    attempts = levels[level]
    return attempts


def options_menu():
    print('(1) Jogar (2) Regras (3) Menu de jogos (4) Sair')
    option = int(input('Insira a opção desejada: '))
    try:
        options = {1 : play, 2: read_rules, 3 : main.main_menu, 4 : quit}
        options[option]()
    except KeyError:
        print('Valor inválido!')
        options_menu()

def options_not_menu():
    print('Opções disponíveis: (1) Jogar (2) Regras (3) Menu (4) Sair')
    option = int(input('Insira a opção desejada: '))
    try:
        options = {1 : play, 2: read_rules, 3 : menu, 4 : quit}
        options[option]()
    except KeyError:
        print('Valor inválido!')
        options_not_menu()

if (__name__ == '__main__'):
    menu()
