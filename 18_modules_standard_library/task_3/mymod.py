def count_lines(file):
    file.seek(0)
    counter = 0
    for _ in file.readlines():
        counter += 1
    return counter


def count_chars(file):
    file.seek(0)
    counter = 0
    for _ in file.read():
        counter += 1
    return counter


def test(name):
    with open(name) as f:
        lines = count_lines(f)
        chars = count_chars(f)
        return f"lines = {lines}, chars = {chars}"
