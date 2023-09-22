import random


def generate_data(n, min=-1000, max=1000):
    data = []
    # mistake: range(0,n+1)
    for _ in range(0, n):
        data.append(random.uniform(min, max))
    return data


def arithmetic_series(n):
    return n * (1 + n) / 2


def insertion(l, verbose):
    def swap_places(l, idx_a, idx_b):
        val_a = l[idx_a]
        l[idx_a] = l[idx_b]
        l[idx_b] = val_a
        return l

    # for each value in unsorted list, starting from index 1
    idx_to_place = 1

    # O N *
    # O some kind of math sequence? sum of 1+2+3+4 (first one compared to one, second to two until last one compared to n-1)
    # ans: arithmetic series = N*N?
    while idx_to_place < len(l):
        val_to_place = l[idx_to_place]

        if verbose:
            print(f"{idx_to_place=}")
        # compare to each value before it
        # mistake: range([start, end[, step)
        # - first wrong start<->end
        # - then didn't consider inclusive/exclusive

        for idx_to_compare_to in range(idx_to_place - 1, -1, -1):
            if verbose:
                print(f"{idx_to_compare_to=}")
            val_to_compare_to = l[idx_to_compare_to]
            if val_to_place <= val_to_compare_to:
                # mistake: swapped with idx_to_place (which stays the same for this inner loop) instead of idx_to_compare_to+1
                l = swap_places(l, idx_to_compare_to, idx_to_compare_to + 1)
            else:
                break

        idx_to_place += 1

    return l


def selection(l: list):
    pass


def bubble(l):
    pass


def skip(l):
    pass


def merge(l):
    pass


def quick(l):
    pass


if __name__ == "__main__":
    # print(arithmetic_series(10))
    input_data = generate_data(4)
    print("Input data:", input_data, "\n", sep="\n")
    sorted_builtin = sorted(input_data)
    sorted_insertion = insertion(input_data, verbose=False)
    print("Builtin sort:", sorted_builtin, "\n", sep="\n")
    print("Insertion sort:", sorted_insertion, "\n", sep="\n")
    print("Insertion same as builtin:", sorted_insertion == sorted_builtin)
    # swap_places(input_data, 0, 3)
    # print("Swapped 0 and 3: ", input_data)
