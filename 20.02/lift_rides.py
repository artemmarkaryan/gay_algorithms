from random import randint
import pprint
pp = pprint.PrettyPrinter().pprint


def main():
    max_weight = 10
    passengers = [1, 2, 3, 4, 5, 6]
    # max_weight = randint(10, 20)
    # passengers = [randint(1, 10) for _ in range(randint(10, 20))]
    passengers_sorted = sorted(passengers)

    selected = {}
    rides = 0
    for i in range(len(passengers_sorted)-1, -1, -1):
        if selected.get(i) is not None: continue
        group_w = passengers[i]
        selected[i] = True
        for j in range(i, -1, -1):
            if selected.get(j) is not None: continue
            if group_w + passengers_sorted[j] <= max_weight:
                    group_w += passengers_sorted[j]
                    selected[j] = True
        rides += 1

    print("->", rides)

main()