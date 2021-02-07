def bubble_sort(array):
    for i in range(len(array)-1):
        for j in range(i+1, len(array)):
            if array[i] > array[j]:
                array[j], array[i] = array[i], array[j]
    return array


if __name__ == '__main__':
    import random

    n = 100
    arr = []
    for i in range(n):
        arr.append(random.randint(0, 50))
    print(arr)
    print(bubble_sort(arr))

