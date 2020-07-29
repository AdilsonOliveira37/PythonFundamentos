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
class Hangman():
    # Método construtor
    def __init__(self, string):
        self.string = string
    # Advinha a letra
    def guess(self, letter):
        letter = input('Qual letra voce escolhe?')
        if letter in self.string:
            return -1
        else :
            return 1
    
    # Verifica se o jogo terminou
    def game_end(self):
        if i == 6:
            return true
    # Verifica se o jogador ganhou
    def winner(self):

    # Não mostra letra no board
    def hide_word(self):

    # Status do game
    def print_game_status(self):

# Função para leitura do banco
def rand_word():
    with open('palavras.txt', 'rt') as f:
        bank = f.readlines()
    return bank[random.randint(0, len(bank))].strip()

def main():
    game = Hangman(rand_word()) 

    game.print_game_status()

    while()

    # De acordo com o resultado, imprime a mensagem na tela
    if game.winner():
        print('\nParabéns você completou a palavra')
    else:
        print('\nGame over!')
        print('\nA palavra era '+ game.string)
    print('Foi bom jogar com você!')

# Executa o programa
if __name__ == '__main__':
    main()