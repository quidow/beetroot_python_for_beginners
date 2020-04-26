from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QWidget
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout


class TicTacToeUi(QMainWindow):

    def __init__(self):
        super().__init__()
        # Set some main window's properties
        self.setWindowTitle('Tic-tac-toe')
        self.setFixedSize(400, 500)
        # Set the central widget and the general layout
        self.generalLayout = QVBoxLayout()
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)
        self._centralWidget.setLayout(self.generalLayout)
        # Create the display and the buttons
        self._createButtons()

    def _createButtons(self):
        self.buttons = {}
        self.controls = {}

        orderLayout = QGridLayout()
        self.controls["first"] = QtWidgets.QRadioButton()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHeightForWidth(self.controls["first"].sizePolicy().hasHeightForWidth())
        self.controls["first"].setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.controls["first"].setFont(font)
        self.controls["first"].setText("First")
        self.controls["first"].setChecked(True)
        orderLayout.addWidget(self.controls["first"], 0, 0, 1, 1)
        self.generalLayout.addLayout(orderLayout)
        self.controls["second"] = QtWidgets.QRadioButton()
        font = QtGui.QFont()
        font.setPointSize(10)
        self.controls["second"].setFont(font)
        self.controls["second"].setText("Second")
        orderLayout.addWidget(self.controls["second"], 0, 1, 1, 1)
        self.generalLayout.addLayout(orderLayout)

        buttonsLayout = QGridLayout()
        buttons = {(0, 0),
                   (0, 1),
                   (0, 2),
                   (1, 0),
                   (1, 1),
                   (1, 2),
                   (2, 0),
                   (2, 1),
                   (2, 2),
                   }
        for pos in buttons:
            self.buttons[pos] = QPushButton()
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Expanding)
            sizePolicy.setHeightForWidth(self.buttons[pos].sizePolicy().hasHeightForWidth())
            self.buttons[pos].setSizePolicy(sizePolicy)
            palette = QtGui.QPalette()
            brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
            self.buttons[pos].setPalette(palette)
            font = QtGui.QFont()
            font.setPointSize(60)
            self.buttons[pos].setFont(font)
            buttonsLayout.addWidget(self.buttons[pos], pos[0], pos[1])
            self.generalLayout.addLayout(buttonsLayout)

        controlLayout = QGridLayout()

        self.controls["user-score-label"] = QtWidgets.QLabel()
        font = QtGui.QFont()
        font.setPointSize(14)
        self.controls["user-score-label"].setFont(font)
        self.controls["user-score-label"].setText("User score:")
        controlLayout.addWidget(self.controls["user-score-label"], 0, 0, 1, 1)
        self.generalLayout.addLayout(controlLayout)

        self.controls["user-score-value"] = QtWidgets.QLabel()
        font = QtGui.QFont()
        font.setPointSize(14)
        self.controls["user-score-value"].setFont(font)
        self.controls["user-score-value"].setText("0")
        controlLayout.addWidget(self.controls["user-score-value"], 0, 1, 1, 1)
        self.generalLayout.addLayout(controlLayout)

        self.controls["comp-score-label"] = QtWidgets.QLabel()
        font = QtGui.QFont()
        font.setPointSize(14)
        self.controls["comp-score-label"].setFont(font)
        self.controls["comp-score-label"].setText("Computer score:")
        controlLayout.addWidget(self.controls["comp-score-label"], 1, 0, 1, 1)
        self.generalLayout.addLayout(controlLayout)

        self.controls["comp-score-value"] = QtWidgets.QLabel()
        font = QtGui.QFont()
        font.setPointSize(14)
        self.controls["comp-score-value"].setFont(font)
        self.controls["comp-score-value"].setText("0")
        controlLayout.addWidget(self.controls["comp-score-value"], 1, 1, 1, 1)
        self.generalLayout.addLayout(controlLayout)

        self.controls["play-again"] = QPushButton()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHeightForWidth(self.controls["play-again"].sizePolicy().hasHeightForWidth())
        self.controls["play-again"].setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.controls["play-again"].setFont(font)
        self.controls["play-again"].setText("Play again")
        controlLayout.addWidget(self.controls["play-again"], 2, 0, 1, 2)
        self.generalLayout.addLayout(controlLayout)

