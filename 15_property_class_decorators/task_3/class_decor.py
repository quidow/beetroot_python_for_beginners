from functools import wraps


class TypeDecorators:

    @staticmethod
    def to_int(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return int(func(args[0]))
            except (ValueError, TypeError):
                return func(args, **kwargs)
        return wrapper

    @staticmethod
    def to_str(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return str(func(args[0]))
            except (ValueError, TypeError):
                return func(args, **kwargs)
        return wrapper

    @staticmethod
    def to_bool(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return bool(func(args[0]))
            except (ValueError, TypeError):
                return func(args, **kwargs)
        return wrapper

    @staticmethod
    def to_float(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return float(func(args[0]))
            except (ValueError, TypeError):
                return func(args, **kwargs)
        return wrapper


@TypeDecorators.to_int
def do_nothing(string: str):
    return string


@TypeDecorators.to_bool
def do_something(string: str):
    return string
