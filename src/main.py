
import random

class Player:
    def __init__(self, name):
        self.name = name
        self.guesses = []

    def make_guess(self):
        pass

class ComputerPlayer(Player):
    def make_guess(self):
        bet = random.randint(1, 100)
        self.guesses.append(bet)
        return bet

class HumanPlayer(Player):
    def make_guess(self):
        while True:
            try:
                bet = int(input("Player, digite seu palpite: "))
                if 1 <= bet <= 100:
                    self.guesses.append(bet)
                    return bet
                else:
                    print("Por favor, digite um número entre 1 e 100.")
            except ValueError:
                print("Por favor, digite um número válido.")

def start_game():
    return random.randint(1, 100)

def check_guess(player, target_number, max_attempts):
    computer_player = ComputerPlayer("Computador The Boss")
    attempts = 0

    while attempts < max_attempts:
        bet = player.make_guess()
        print(player.name + " seu palpite foi:", bet)
        attempts += 1

        if bet == target_number:
            print("UHUU VOCÊ CONSEGUIU " + player.name + "! " + "O número correto é:", bet)
            display_game_result(player)
            return
        elif bet < target_number:
            print("Muito baixo!")
        else:
            print("Muito alto!")

        # Alternar entre o player e o computador
        player, computer_player = computer_player, player

    if attempts >= max_attempts:
        print("Fim de jogo! O número de tentativas máximo foi alcançado.")
        display_game_result(computer_player)

def display_game_result(winner):
    print("RESUMO DA PARTIDA!")
    print(winner.name + " Aqui vai o resumo da partida.")
    print("Tentativas de " + winner.name + ": " + str(len(winner.guesses)))
    bet_resume(winner)

def bet_resume(player):
    print(player.name + " seus palpites foram:", end=" ")
    print("!".join(map(str, player.guesses)) + "!")

def main():
    target_number = start_game()
    print("BEM VINDO AO GUESS THE NUMBER!")
    print("O número foi sorteado. São quinze rodadas. Tente acertá-lo.")
    print("O Computador é o seu adversário.")
    print("Pressione Enter para começar ou digite qualquer outra coisa para sair.")

    input_text = input()
    if input_text == "":
        player = HumanPlayer("Jogador")
        max_guesses = 15
        check_guess(player, target_number, max_guesses)
    else:
        print("Reiniciando o jogo...")
        main()

if __name__ == "__main__":
    main()
