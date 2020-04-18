def with_index(iterable, start=0):
    if hasattr(iterable, "__iter__"):
        for e in iterable:
            yield start, e
            start += 1
    else:
        raise TypeError
