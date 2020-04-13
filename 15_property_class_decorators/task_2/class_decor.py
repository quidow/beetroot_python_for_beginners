class Boss:

    def __init__(self, id_: int, name: str, company: str):
        self.id = id_
        self.name = name
        self.company = company
        self.workers = []

    @property
    def workers(self):
        return self.__workers

    @workers.setter
    def workers(self, workers):
        if isinstance(workers, list) and all(isinstance(x, Worker) for x in workers):
            self.__workers = workers
        else:
            raise TypeError

    def add_worker(self, worker):
        if isinstance(worker, Worker):
            self.__workers = self.workers + [worker]
        else:
            raise TypeError

    def __str__(self):
        return f"<Boss: {self.name}>"

    def __repr__(self):
        return self.__str__()


class Worker:

    def __init__(self, id_: int, name: str, company: str, boss: Boss):
        if isinstance(id_, int):
            self.id = id_
        else:
            raise TypeError
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError
        if isinstance(company, str):
            self.company = company
        else:
            raise TypeError
        self.boss = boss

    @property
    def boss(self):
        return self.__boss

    @boss.setter
    def boss(self, boss):
        if isinstance(boss, Boss):
            self.__boss = boss
            boss.add_worker(self)
        else:
            raise TypeError

    def __str__(self):
        return f"<Worker: {self.name}>"

    def __repr__(self):
        return self.__str__()
