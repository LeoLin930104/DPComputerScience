import random


def linear_search(l: list, val: int) -> int:
    for i, v in enumerate(l):
        if v == val:
            return i
    return -1


# Precondiction: list must be sorted
def binary_search(l: list, val: int, start: int = 0, end: int = None) -> int:
    # Giving End Value
    if end is None:
        end = len(1) - 1

    # Find middle of list
    mid = start + (end - start) // 2

    # Search Recursively
    if end >= start:
        # Found Value
        if l[mid] == val:
            return mid
        # Search the Right Side of the List
        elif l[mid] < val:
            return binary_search(l, val, start=mid + 1, end=end)
        # Search the Right Side of the List
        elif l[mid] > val:
            return binary_search(l, val, start=start, end=mid - 1)
    return -1


if __name__ == "__main__":
    trial_size = 20
    target = 10
    values = []
    for i in range(trial_size):
        values.append(random.randint(0, trial_size))
    values.sort()

    index = linear_search(values, target)
    print(f"Values: {values}, Target: {target}, Index: {index}")

    index = binary_search(values, 10, 0, len(values))
    print(f"Values: {values}, Target: {target}, Index: {index}")
