def in_range(start, end, step=1):
    if (
        isinstance(start, int)
        and isinstance(end, int)
        and isinstance(step, int)
    ):
        if step > 0:
            while start <= end:
                yield start
                start += step
        elif step < 0:
            while start >= end:
                yield start
                start += step
        else:
            raise ValueError
    else:
        raise TypeError
