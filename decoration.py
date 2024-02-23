from time import time


def decorate(fn):
    def inner(*args, **kwargs):
        print("********************")
        print(fn(*args, **kwargs))
        print("********************")

    return inner


@decorate
def show_name(name):
    return name


show_name("miriam")


def time_taken(func):
    def wrap(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f"it took {t2 - t1:.3f}ms to execute")
        return result

    return wrap


@time_taken
def get_list(number):
    result = []
    for i in range(number):
        result.append(i)
    return result


get_list(10000000)


def gun(name, number=0000):
    return f'{name} & {number}'


gun("baliqis")
print(gun)
