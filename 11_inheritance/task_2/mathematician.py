class ListWorker:

    def filter_list(self, list_arg, key):
        if not isinstance(list_arg, list) or not all(isinstance(x, int) for x in list_arg):
            raise TypeError
        return list(filter(key, list_arg))

    def map_list(self, list_arg, key):
        if not isinstance(list_arg, list) or not all(isinstance(x, int) for x in list_arg):
            raise TypeError
        return list(map(key, list_arg))


class Mathematician(ListWorker):

    def square_nums(self, number_list):
        key = lambda x: x ** 2
        return self.map_list(number_list, key)

    def remove_positives(self, number_list):
        key = lambda x: x < 0
        return self.filter_list(number_list, key)

    def filter_leaps(self, number_list):
        key = lambda x: x % 4 == 0 and (x % 100 != 0 or x % 400 == 0)
        return self.filter_list(number_list, key)
