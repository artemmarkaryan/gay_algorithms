import random


class Matrix:
    def __init__(self, size):
        self.field = [
            [random.randint(0, 9) for _ in range(size)]
            for __ in range(size)
        ]

    def __str__(self):
        out = ""
        for row in self.field:
            for el in row:
                out += str(el) + "  "
            out += "\n"
        return out


def best(x, y):
    if x + y == 0:
        return m.field[x][y]
    elif x == 0:
        return best(x, y-1) + m.field[x][y]
    elif y == 0:
        return best(x-1, y) + m.field[x][y]
    else:
        return max(best(x, y-1), best(x-1, y)) + m.field[x][y]


while 1:
    n = int(input())
    cache = [
        [0 for _ in range(n)]
        for __ in range(n)
    ]
    m = Matrix(n)

    print(m)
    print(best(n-1, n-1))