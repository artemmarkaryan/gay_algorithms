def check_sort(array):
    for i in range(len(array)-1):
        if array[i] > array[i+1]:
            return False
    return True


def binary_search(array, element):
    if check_sort(array):
        a, b = 0, len(array)
        while a < b:
            i = (a+b) // 2
            print(f'a: {a}, b: {b}, i: {i}')
            if array[i] > element:
                b = i
            elif array[i] < element:
                a = i
            else:
                return i
    return "not found"


if __name__ == '__main__':
    print(
        binary_search([1, 2, 3, 4, 5], 1)
    )