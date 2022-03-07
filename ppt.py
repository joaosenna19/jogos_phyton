import random
import main


def menu():
    print('********************************************')
    print('Bem vindo ao jogo de Pedra, Papel e Tesoura!')
    print('********************************************')

    options_menu()


def read_rules():
    print('************************')
    print('Regras do Pedra, Papel e Tesoura.')
    print('************************')
    print('(1) Você deve escolher entre pedra, papel ou tesoura.')
    print('(2) Ganha quem vencer o outro três vezes primeiro.')
    print('(3) Divirta-se!')

    options_not_menu()


def play():
    computer_score = 0
    player_score = 0
    options = ['pedra', 'papel', 'tesoura']

    while True:
        computer_choice = options[random.randint(0, 2)].lower()
        player_choice = str(input('Escolha sua arma: ')).strip().lower()

        if(player_choice not in options):
            continue

        if(player_choice == 'pedra' and computer_choice == 'tesoura'):
            turn_won_by_player(computer_choice)
            player_score += 1
        elif(player_choice == 'tesoura' and computer_choice == 'papel'):
            turn_won_by_player(computer_choice)
            player_score += 1
        elif(player_choice == 'papel' and computer_choice == 'pedra'):
            turn_won_by_player(computer_choice)
            player_score += 1
        elif(player_choice == computer_choice):
            print('Empate.')
        else:
            turn_won_by_computer(computer_choice)
            computer_score += 1

        show_points(computer_score, player_score)

        if(player_score == 3):
            print(f'Você venceu!. Você fez {player_score} pontos primeiro que o computador.')
            break
        elif(computer_score == 3):
            print(f'Você perdeu! O computador fez {computer_score} pontos primeiro que você.')
            break

    print('Fim de jogo!')

    options_not_menu()


def turn_won_by_player(computer_choice):
    print('Você venceu essa rodada. O computador jogou {}.'.format(computer_choice))


def turn_won_by_computer(computer_choice):
    print('Você perdeu essa rodada. O computador jogou {}.'.format(computer_choice))


def show_points(computer_score, player_score):
    print('Pontuação:')
    print('Computador: {}.'.format(computer_score))
    print('Jogador: {}.'.format(player_score))


def options_menu():
    print('(1) Jogar (2) Regras (3) Menu de jogos (4) Sair')
    option = int(input('Insira a opção desejada: '))
    try:
        options = {1: play, 2: read_rules, 3: main.main_menu, 4: quit}
        options[option]()
    except KeyError:
        print('Valor inválido!')
        options_menu()


def options_not_menu():
    print('Opções disponíveis: (1) Jogar (2) Regras (3) Menu (4) Sair')
    option = int(input('Insira a opção desejada: '))
    try:
        options = {1: play, 2: read_rules, 3: menu, 4: quit}
        options[option]()
    except KeyError:
        print('Valor inválido!')
        options_not_menu()


if(__name__ == '__main__'):
    menu()