class CustomException(Exception):

    def __init__(self, msg):
        with open("logs.txt", "a") as f:
            f.write(msg + "\n")
