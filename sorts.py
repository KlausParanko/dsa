import random


def generate_data(n, min=-1000, max=1000):
    data = []
    for _ in range(0, n + 1):
        data.append(random.uniform(min, max))
    return data


def insertion():
    pass


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


input_data = generate_data(50)
print("Input data:\n\n", input_data)
print("\n\nBuiltin sort:\n\n", sorted(input_data))
