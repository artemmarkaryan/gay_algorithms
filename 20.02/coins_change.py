n = int(input())
coins = list(
    map(
        int,
        input().split()
    )
)


def solve(x):
    if x == 0:
        return 0
    elif x < 0:
        return n + 1
    return min([
        solve(x - coin) + 1 for coin in coins
    ])


print(solve(n))