# Оптимальная стратегия - брать наибольшее число
# Решено

t = int(input())
for _ in range(t):
    __ = input()
    a = b = 0
    n = sorted(list(map(int, input().split())))
    for i in range(len(n)-1, -1, -2):
        a += n[i] if not n[i] % 2 else 0
    for i in range(len(n)-2, -1, -2):
        b += n[i] if n[i] % 2 else 0
    if a > b:
        print("Alice")
    elif b > a:
        print("Bob")
    else:
        print("Tie")





