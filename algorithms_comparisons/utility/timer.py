import time
def timed(func):
    def wrapper(*args):
        start = time.time()
        res = func(*args)
        end = time.time()
        ellapsed = end - start
        return res, ellapsed
    return wrapper