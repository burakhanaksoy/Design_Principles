import unittest


class Singleton(type):
    _instance = {}

    def __call__(cls, *args, **kwargs):

        if cls not in cls._instance:
            cls._instance[cls] = super(
                Singleton, cls).__call__(*args, **kwargs)

        return cls._instance[cls]


class Database(metaclass=Singleton):

    _db = {
        'Tokyo': 34000000,
        'Istanbul': 17000000,
        'NewYork': 23000000,
        'Osaka': 19000000
    }

    def __init__(self):
        print('Loading database...')


class RecordFinder():
    def find_total_population(self, cities):

        result = 0
        for c in cities:
            result += Database()._db[c]

        return result


class SingletonTests(unittest.TestCase):

    def test_is_singleton(self):
        db1 = Database()
        db2 = Database()

        self.assertEqual(db1, db2)

    def test_total_population(self):
        rf = RecordFinder()

        res = rf.find_total_population(['Tokyo', 'Osaka'])
        expected = 34000000 + 19000000

        self.assertEqual(res, expected)


if __name__ == '__main__':
    unittest.main()
