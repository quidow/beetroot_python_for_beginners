import sys
from PyQt5.QtWidgets import QApplication
from tictactoeui import TicTacToeUi
from tictactoectrl import TicTacToeCtrl

if __name__ == '__main__':
    def my_exception_hook(exctype, value, traceback):
        # Print the error and traceback
        print(exctype, value, traceback)
        # Call the normal Exception hook after
        sys._excepthook(exctype, value, traceback)
        sys.exit(1)


    # Back up the reference to the exceptionhook
    sys._excepthook = sys.excepthook

    # Set the exception hook to our wrapping function
    sys.excepthook = my_exception_hook

    tictactoe = QApplication(sys.argv)
    view = TicTacToeUi()
    view.show()
    TicTacToeCtrl(view=view)
    sys.exit(tictactoe.exec_())
