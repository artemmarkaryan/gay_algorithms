n = list(
    map(
        int,
        input().split()
    )
)

foo = [1 for _ in range(len(n))]
flag_increasing = True
sequence = 1
max_i = 0
for i in range(1, len(n)):
    max_j = 0
    for j in range(0, i):
        if n[j] < n[i]:
            max_j = max(max_j, foo[j])
    foo[i] += max_j
    max_i = max(max_i, foo[i])

print(max_i)