from functools import partial
import random


def stop(func):
    def wrapper(self, *args, **kwargs):
        if not self.stop_game:
            return func(self, *args, **kwargs)
    return wrapper


class TicTacToeCtrl:

    def __init__(self, view):
        self._view = view
        self.stop_game = False
        self._player_mark = "X"
        self._comp_mark = "O"
        self._connectSignals()

    def _new_game(self, choose_order=True):
        for btn in self._view.buttons.values():
            btn.setText("")
            btn.setStyleSheet("")
        for btn in self._view.buttons.values():
            btn.setDisabled(False)
        self.stop_game = False
        if choose_order:
            self._choose_order()

    def _get_btn_array(self):
        for i in range(3):
            yield [self._view.buttons[i, j] for j in range(3)]
            yield [self._view.buttons[j, i] for j in range(3)]
        yield [self._view.buttons[j, j] for j in range(3)]
        yield [self._view.buttons[0, 2], self._view.buttons[1, 1], self._view.buttons[2, 0]]

    def _choose_order(self, new_game=False):
        if new_game:
            self._new_game(choose_order=False)
        if self._view.controls["first"].isChecked():
            choice = "First"
        elif self._view.controls["second"].isChecked():
            choice = "Second"
        if choice == "First":
            self._player_mark = "X"
            self._comp_mark = "O"
        elif choice == "Second":
            self._player_mark = "O"
            self._comp_mark = "X"
            self._comp_turn()
            self._check_result()

    @stop
    def _check_result(self):
        for btn_array in self._get_btn_array():
            btn_set = set(btn.text() for btn in btn_array)
            if len(btn_set) == 1 and "" not in btn_set:
                self.stop_game = True
                for btn in self._view.buttons.values():
                    btn.setDisabled(True)
                if self._player_mark in btn_set:
                    for btn in btn_array:
                        btn.setStyleSheet("background-color: green")
                    self._view.controls["user-score-value"].setText(
                        str(int(self._view.controls["user-score-value"].text()) + 1))
                    break
                elif self._comp_mark in btn_set:
                    for btn in btn_array:
                        btn.setStyleSheet("background-color: red")
                    self._view.controls["comp-score-value"].setText(
                        str(int(self._view.controls["comp-score-value"].text()) + 1))
                    break

    @stop
    def _set_val(self, btn, partial):
        if not btn.text():
            btn.setText(self._player_mark)
            self._check_result()
            self._comp_turn()
            self._check_result()

    @stop
    def _comp_turn(self):
        for btn_array in self._get_btn_array():
            if ([btn.text() for btn in btn_array].count(self._comp_mark) == 2
                    and [btn.text() for btn in btn_array].count(self._player_mark) == 0):
                [btn for btn in btn_array if btn.text() == ""][0].setText(self._comp_mark)
                return
        for btn_array in self._get_btn_array():
            if ([btn.text() for btn in btn_array].count(self._player_mark) == 2
                    and [btn.text() for btn in btn_array].count(self._comp_mark) == 0):
                [btn for btn in btn_array if btn.text() == ""][0].setText(self._comp_mark)
                return
        buttons = [btn for btn in self._view.buttons.values() if not btn.text()]
        if buttons:
            random.choice(buttons).setText(self._comp_mark)

    def _connectSignals(self):
        for btn in self._view.buttons.values():
            btn.clicked.connect(partial(self._set_val, btn))
        self._view.controls["first"].clicked.connect(lambda: self._choose_order(new_game=True))
        self._view.controls["second"].clicked.connect(lambda: self._choose_order(new_game=True))
        self._view.controls["play-again"].clicked.connect(lambda: self._new_game())
