# 1, 2, -1, -2 => 6, 8, 6, 8 ;
# 1, 2 => 2, 1
# 0 + 1 + 2 + 3 = 6
# 1 + 0 + 3 + 4 = 8
# 2 + 3 + 0 + 1 = 6
# 3 + 4 + 1 + 0 = 8

# 2, 1, -1, -2 => 8, 6, 8, 6
# -1, 1, -2, 2 => 6, 6, 8, 8
#
# def foo(arr):
#     r = []
#     for i in range(len(arr)):
#         a = 0
#         for j in range(len(arr)):
#             a += abs(arr[i] - arr[j])
#         r.append(a)
#     return r


# print(foo([1, -1, 2, -2]))
# print(foo([1, -1, 3, -3]))
# print(foo([1, -1, 4, -4]))
# print(foo([1, -1, 20, -20]))
#
# print(foo([1, -1, 5, -5, 20, -20]))
# print(foo([1, -1, 10, -10, 20, -20]))
# print(foo([1, -1, 15, -15, 20, -20]))
# print(foo([1, -1, 17, -17, 20, -20]))
#
# print(foo([1, -1, 2, -2, 3, -3, 4, -4]))
# print(foo([1, -1, 3, -3, 5, -5, 7, -7]))

# max_2 = max_1 * n
# min_2 = sum(abs(n_i))

t = int(input())
for _ in range(t):
    __ = input()
    n = sorted(
        list(set(map(int, input().split())))
    )
    for i in range(len(n)-1, -1, -1):
        max_el = n[]




