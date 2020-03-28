"""
Печать текста псевдографикой

#   #     ####    ####
###      #    #    #
#   #     ####    ####
на несколько колонок. экземпляр класса знает свою ширину, как себя в скольки колонках выводить.
И еще один класс который говорит ширину экрана и хранит массив букв выводимых.
Можно подумать о бегущей строке.
"""

from char_display import CharDisplay
from pseudo_char import PseudoChar

if __name__ == "__main__":
    board = CharDisplay()
    board.add(PseudoChar("a"))
    board.add(PseudoChar("b"))
    board.add(PseudoChar("c"))
    board.set_width(5)
    print(board)
    board.set_width(0)  # returns auto width
    print(board)
