class CharDisplay:

    def __init__(self, *chars, width=None):
        self.chars = list(chars)
        self.auto_width = 0
        self.custom_width = width if width else 0
        for char in chars:
            self.add(char)

    def add(self, char):
        self.chars.append(char)
        self.auto_width += char.width

    def set_width(self, width):
        if type(width) is not int or width < 0:
            raise ValueError
        else:
            self.custom_width = width

    def __str__(self):
        board_lines = [char.char_str.split("\n") for char in self.chars]
        str_board = ""
        for s in zip(*board_lines):
            str_line = " ".join(s)
            if self.custom_width:
                str_line = str_line[:self.custom_width + 1] if len(str_line) > self.custom_width else str_line
            str_board += str_line + "\n"
        return str_board
