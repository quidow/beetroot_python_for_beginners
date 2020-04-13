import re


class User:

    def __init__(self, name, email):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError
        if self.validate(email):
            self.email = email
        else:
            raise TypeError

    @staticmethod
    def validate(email):
        email_regex = re.compile(r"[^@]+@[^@]+\.[^@]+")
        return email_regex.match(email)
