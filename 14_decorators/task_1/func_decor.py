def logger(func):
    def wrapper(*args, **kwargs):
        str_log = f"{func.__name__}  called with: "
        if args or kwargs:
            if args:
                str_log += ', '.join(str(i) for i in args)
            if kwargs:
                if args:
                    str_log += ", "
                str_log += ', '.join(str(k) + ": " + str(e) for k, e in kwargs.items())
        else:
            str_log += "no arguments"
        print(str_log)
        return func(*args, **kwargs)
    return wrapper


@logger
def add(x, y):
    return x + y


@logger
def square_all(*args):
    return [arg ** 2 for arg in args]