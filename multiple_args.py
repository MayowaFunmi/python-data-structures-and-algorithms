def add(*args):
    sum = 0
    for i in range(len(args)):
        sum += args[i]
    return sum

print(add(3, 4, 5, 6))


def all_values(**args):
    for x in args:
        print('Variable name is :', x, ' and value is :', args[x])

all_values(a=4, b='more', c=6.87)
