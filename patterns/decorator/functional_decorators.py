import time
from functools import wraps


def time_taken(func):
    @wraps(func)
    def wrapper():
        start = time.time()
        result = func()
        end = time.time()
        print(f'Time taken: {(end-start):3f}s')
        return result
    return wrapper


def disconnect(func):
    @wraps(func)
    def wrapper():
        result = func()
        print(f'disconnected...')
        return result
    return wrapper


@disconnect
@time_taken
def some_op():
    print('do something')
    time.sleep(1)
    print('finish operation')
    return 123


if __name__ == '__main__':
    some_op()
