def counter():
    count = 0

    def add():
        nonlocal count
        count += 1
        return count

    return add
