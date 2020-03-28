PSEUDO_CHARS = {
    ("a", "A"): " ####\n#    #\n######\n#    #\n#    #",
    ("b", "B"): "#####\n#    #\n#####\n#    #\n#####",
    ("c", "C"): " ####\n#    #\n#\n#    #\n ####"
}


class PseudoChar:

    def __init__(self, char):
        for k, v in PSEUDO_CHARS.items():
            if char in k:
                char_str = v
                break
        else:
            raise ValueError
        char_lines = char_str.split("\n")
        self.width = len(max(char_lines, key=len))
        char_lines = [e.ljust(self.width, " ") for e in char_lines]
        self.char_str = "\n".join(char_lines)
