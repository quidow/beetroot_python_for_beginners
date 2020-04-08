def arg_rules(type_: type, max_length: int, contains: list):
    def wrapper(func):
        def wrapped(*args, **kwargs):
            arg_str = args[0] or kwargs["name"]
            if not isinstance(arg_str, type_):
                print(f"Arg \"name\" for function {func.__name__} is not {type_}")
                return False
            if len(arg_str) > max_length:
                print(f"Arg \"name\" for function {func.__name__} has len more than 15")
                return False
            for e in contains:
                if e not in arg_str:
                    print(f"Arg \"name\" for function {func.__name__} does not contain {e}")
                    return False
            return func(*args, **kwargs)
        return wrapped
    return wrapper


@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"
