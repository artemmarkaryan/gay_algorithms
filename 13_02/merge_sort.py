def merge(array1, array2):
    array = []
    while True:
        if len(array1) == 0:
            array += array2
            break
        if len(array2) == 0:
            array += array1
            break

        if array1[0] < array2[0]:
            array.append(array1.pop(0))
        else:
            array.append(array2.pop(0))

    return array


def merge_sort(array):
    if len(array) == 1:
        return array
    elif len(array) == 2:
        if array[0] > array[1]:
            array[0], array[1] = array[1], array[0]
        return array
    else:
        return merge(
            merge_sort(array[:len(array)//2]),
            merge_sort(array[len(array)//2:])
        )


if __name__ == '__main__':
    import random

    n = 5
    arr = []
    for i in range(n):
        arr.append(random.randint(0, 50))
    print(arr)
    print(merge_sort(arr))
