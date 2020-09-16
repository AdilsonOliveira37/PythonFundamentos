import random

#Forca
board = ['''
------------->>Hangman<<--------------

 +----+
 |    |
      |
      |
      |
      |
==============''','''
 +----+
 |    |
 O    |
      |
      |
      |
==============''','''
 +----+
 |    |
 O    |
 |    |
      |
      |
==============''','''
 +----+
 |    |
 O    |
/|    |
      |
      |
==============''','''
 +----+
 |    |
 O    |
/|\   |
      |
      |
==============''','''
 +----+
 |    |
 O    |
/|\   |
/     |
      |
==============''','''
 +----+
 |    |
 O    |
/|\   |
/ \   |
      |
==============''']

#Classe da forca
class Hangman:
    # Metodo construtor
    def __init__(self, word):
        self.word = word
        self.missed_letters = []
        self.guessed_leters = []

    # Advinha a letra
    def guess(self, letter):
        letter = input('Qual letra voce escolhe?')
        if letter in self.word and letter not in self.guessed_leters:
            self.guessed_leters.append(letter)
        elif letter not in self.word and letter not in self.missed_letters:
            self.missed_letters.append(letter)
        else: 
            return False
        return True

    # Verifica se o jogo terminou
    def game_end(self):
        return self.winner() or (len(self.missed_letters) == 6)
    # Verifica se o jogador ganhou
    def winner(self):
        if '_' not in self.hide_word():
            return True
        return False

    # Nao mostra letra no board
    def hide_word(self):
        rtn = ''
        for letter in self.word:
            if letter not in self.guessed_leters:
                rtn += '_'
            else:
                rtn += letter
            return rtn

    # Status do game
    def print_game_status(self):
        print(board[len(self.missed_letters)])
        print('\nPalavra: '+ self.hide_word())
        print('\nLetras erradas: ')
        for letter in self.missed_letters:
            print(letter)
        print()
        print('\nLetras corretas: ')
        for letter in self.guessed_leters:
            print(letter)
        print()

# Funcao para leitura do banco
def rand_word():
    with open('palavras.txt', 'rt') as f:
        bank = f.readlines()
    return bank[random.randint(0, len(bank))].strip()

def main():
    game = Hangman(rand_word()) 

    while not game.winner():
        game.print_game_status()
        user_input = raw_input('\nDigite a letra que voce escolheu:')
        game.guess(user_input)

    # De acordo com o resultado, imprime a mensagem na tela
    if game.winner():
        print('\nParabens voce completou a palavra')
    else:
        print('\nGame over!')
        print('\nA palavra era '+ game.word)
    print('Foi bom jogar com voce!')

# Executa o programa
if __name__ == '__main__':
    main()