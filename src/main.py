import random
import time


# Classe pai para os jogadores
class Player:
    def __init__(self, name):
        self.name = name
        self.guesses = []  #Lista para armazenar os palpites dos jogadores

    def make_guess(self):
        pass  #Método a ser implementado pelas classes filhas

#Classe para o jogador computador
class ComputerPlayer(Player):
    def make_guess(self):
        # O computador faz um palpite aleatório entre 1 e 100
        bet = random.randint(1, 100)
        self.guesses.append(bet)  # Armazena o palpite na lista de palpites
        return bet

# Classe para o jogador humano


class HumanPlayer(Player):
    def make_guess(self):
        while True:
            try:
                # O jogador humano digita seu 
                #input('Você começa!')
                bet = int(input('Player, digite seu palpite: '))
                if 1 <= bet <= 100:
                    # Armazena o palpite válido na lista de palpites
                    self.guesses.append(bet)
                    return bet
                else:
                    print('Por favor, digite um número entre 1 e 100.')
            except ValueError:
                print('Por favor, digite um número válido.')

# Função para iniciar o jogo com um número aleatório entre 1 e 100


def start_game():
    return random.randint(1, 100)

# Função para verificar o palpite do jogador e determinar se ele acertou ou não


def check_guess(player, target_number, max_attempts):
    computer_player = ComputerPlayer('Computador The Boss')
    attempts = 0

    while attempts < max_attempts:
        bet = player.make_guess()  # O jogador faz um palpite
        print(player.name + ' seu palpite foi:', bet)
        attempts += 1

        if bet == target_number:
            print('UHUU VOCÊ CONSEGUIU ' + player.name +
                  '! ' + 'O número correto é:', bet)
            display_game_result(player)
            return
        elif bet < target_number:
            print('Muito baixo!')
        else:

            print('Muito alto!')\

       # Introduzindo uma pausa de 1 segundo antes de alternar para o próximo jogador
        time.sleep(1)

        print()
        # Alternância entre o jogador e o computador
        player, computer_player = computer_player, player

    if attempts >= max_attempts:
        print('Fim de jogo! O número de tentativas máxima foi alcançada.')
        display_game_result(computer_player)
        

# Função para exibir o resumo da partida


def display_game_result(winner):
    print('RESUMO DA PARTIDA!')
    print(winner.name + ' Aqui vai o resumo da partida.')
    print('Tentativas de ' + winner.name + ': ' + str(len(winner.guesses)))
    bet_resume(winner)

# Função para exibir os palpites feitos pelo jogador


def bet_resume(player):
    print(player.name + ' seus palpites foram:', end=' ')
    print('!'.join(map(str, player.guesses)) + '!')

# Função principal do jogo


def main():
    target_number = start_game()
    print()
    print('BEM VINDO AO GUESS THE NUMBER!')
    print()
    print('O número foi sorteado. São dez rodadas. Tente acertá-lo.')
    print('O Computador é o seu adversário.')
    print('Pressione Enter para começar ou digite qualquer outra coisa para sair.')

    input_text = input()
    if input_text == '':
        player = HumanPlayer('Jogador')
        max_guesses = 10  # Número máximo de tentativas permitidas
        check_guess(player, target_number, max_guesses)
    else:
        print('Reiniciando o jogo...')
        main()


if __name__ == '__main__':
    main()
