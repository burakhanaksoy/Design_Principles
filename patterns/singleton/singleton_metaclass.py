class Singleton(type):
    _instance = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instance:
            cls._instance[cls] = super(
                Singleton, cls).__call__(*args, **kwargs)

        return cls._instance[cls]


class Database(metaclass=Singleton):
    def __init__(self):
        print('Creating database...')


if __name__ == '__main__':
    db1 = Database()
    db2 = Database()
    print(db1 == db2)
