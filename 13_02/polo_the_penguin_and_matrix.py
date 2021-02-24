# Решено
import pprint
import cmath

flag_possible = True
n, m, d = list(map(int, input().split()))
# Matrix n to m, can subtract or add d
# sum(abs(n_i - x)) -> min for n_i in n

min_el = cmath.inf
arr_el = []
for _ in range(n):
    for el in map(int, input().split()):
        min_el = min(min_el, el)
        arr_el.append(el)

for el in arr_el:
    if (el - min_el) % d != 0:
        flag_possible = False
        break

if flag_possible:
    sorted_arr = sorted(arr_el)
    base_el = sorted_arr[len(sorted_arr)//2]
    moves = 0
    for el in arr_el:
        moves += abs((el - base_el)) // d
    print(moves)
else:
    print(-1)
