import sys
from PyQt5.QtWidgets import QApplication
from pycalcui import PyCalcUi
from pycalcctrl import PyCalcCtrl, evaluateExpression

if __name__ == '__main__':
    """Main function."""
    # Create an instance of `QApplication`
    pycalc = QApplication(sys.argv)
    # Show the calculator's GUI
    view = PyCalcUi()
    view.show()
    # Create instances of the model and the controller
    model = evaluateExpression
    PyCalcCtrl(model=model, view=view)
    # Execute calculator's main loop
    sys.exit(pycalc.exec_())
