from typing import Callable
import time

def lead_time(func: Callable):
    def inner(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        print(f'Выполнения заняло {end - start} секунд')
        return res
    return inner