# timethis.py
import functools


def timethis(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        import time
        start = time.time()
        r = func(*args, **kwargs)
        end = time.time()
        print('%s.%s: %f' % (func.__module__, func.__name__, end-start))
        return r
    return wrapper


def timethis2(func):
    def wrapper(*args, **kwargs):
        import time
        start = time.time()
        r = func(*args, **kwargs)
        end = time.time()
        print('%s.%s: %f' % (func.__module__, func.__name__, end-start))
        return r
    return wrapper

@timethis
def countdown(n):
    while n > 0:
        n -= 1

@timethis2
def countdown2(n):
    while n > 0:
        n -= 1

t=countdown(10000000)
print(t)
print(countdown.__name__)

countdown2(10000000)
print(countdown2.__name__)
