digits = list(range(1, 51))


# def check_even(number):
#     return number % 2 == 0


# print(list(filter(lambda number: number % 2 == 0, digits)))

def jumoke(p):
    return p ** 2


print(list(map(jumoke, digits)))
print(list(map(lambda p: p ** 2, digits)))
