import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.guesses = []

    def make_guess(self):
        pass

class ComputerPlayer(Player):
    def make_guess(self):
        return random.randint(1, 100)

class HumanPlayer(Player):
    def make_guess(self):
        while True:
            try:
                bet = int(input('{}, digite seu palpite: '.format(self.name)))
                if 1 <= bet <= 100:
                    self.guesses.append(bet)
                    return bet
                else:
                    print('Por favor, digite um número entre 1 e 100.')
            except ValueError:
                print('Por favor, digite um número válido.')

def check_guess(player, target_number):
    bet = player.make_guess()
    print(player.name + ', seu palpite foi:', bet)

    if bet == target_number:
        print('Parabéns {}, você acertou! O número correto é: {}'.format(player.name, bet))
        display_game_result(player)
        return True
    elif bet < target_number:
        print('Muito baixo!\n')
    else:
        print('Muito alto!\n')

    return False

def switch_player(current_player):
    if isinstance(current_player, HumanPlayer):
        return ComputerPlayer('Computador The Boss')
    else:
        return HumanPlayer('Jogador')

def display_game_result(winner):
    print('RESUMO DA PARTIDA!')
    print('{} Aqui vai o resumo da partida.'.format(winner.name))
    print('Tentativas de {}: {}'.format(winner.name, len(winner.guesses)))
    print('{} seus palpites foram: {}'.format(winner.name, ' '.join(map(str, winner.guesses))))

def start_game():
    return random.randint(1, 100)

def main():
    target_number = start_game()
    
    print('BEM VINDO AO GUESS THE NUMBER!\n')
    print('O número foi sorteado. São dez rodadas. Tente acertá-lo.\n')
    print('O Computador é o seu adversário.')
    print('Pressione Enter para começar ou digite qualquer outra coisa para sair.')

    input_text = input()
    if input_text == '':
        player = HumanPlayer('Jogador')
        attempts = 0
        max_attempts = 10
        while attempts < max_attempts:
            if check_guess(player, target_number):
                return
            player = switch_player(player)
            attempts += 1

        print('Fim de jogo! O número máximo de tentativas foi alcançado.')
        display_game_result(switch_player(player))
    else:
        print('Reiniciando o jogo...')
        main()

if __name__ == '__main__':
    main()
