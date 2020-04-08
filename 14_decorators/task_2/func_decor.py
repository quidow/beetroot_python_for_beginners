def stop_words(words: list):
    def wrapper(func):
        def wrapped(*args, **kwargs):
            ret_str = func(*args, **kwargs)
            for stop_word in words:
                ret_str = ret_str.replace(stop_word, "*")
            return ret_str
        return wrapped
    return wrapper


@stop_words(['pepsi', 'BMW'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"
