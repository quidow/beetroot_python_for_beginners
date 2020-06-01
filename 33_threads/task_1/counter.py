import threading


class Counter(threading.Thread):
    counter = 0
    rounds = 100000

    @classmethod
    def run(cls):
        for _ in range(cls.rounds):
            cls.counter += 1
