import random


def swap(l: list, i: int, j: int):
    l[i], l[j] = l[j], l[i]


def bubble_sort(l: list):
    swapped = True
    end = len(l) - 1
    # Repeat loop while we find elements to swap
    # Stop when nothing has been swapped
    while swapped:
        # We haven't swapped anything yet so set swapped to false
        swapped = False
        for i in range(end):
            j = i + 1
            if l[i] > l[j]:
                swap(l, i, j)
                swapped = True
        end -= 1


def selection_sort(l: list):
    # for each element in the array (except last)
    for i in range(len(l) - 1):
        # assume value at i is the smallest
        m = i
        # look through all other elements for smaller value
        for j in range(i, len(l)):
            if l[j] < l[m]:
                m = j
        # If we found a smaller value, swap values at i and m
        if m != i:
            swap(l, i, m)


def insertion_sort(l: list):
    # Start at the 2nd element of the array
    for i in range(1, len(l)):
        current = l[i]
        j = i - 1
        # while we find values greater than current, move values over 1
        while j >= 0 and current < l[j]:
            l[j + 1] = l[j]
            j -= 1
        # Insert current in correct place
        l[j + 1] = current


def merge_sort(l: list):
    if len(l) > 1:
        # find middle
        mid = len(l) // 2
        # split into a left list and right list
        L = l[:mid]
        R = l[mid:]

        # Sort left side
        merge_sort(L)
        # Sort right side
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            # If value in left array < value in right array
            if L[i] < R[j]:
                l[k] = L[i]
                i += 1
            else:
                l[k] = R[j]
                j += 1
            k += 1

        # Copy whatever remains in the list that did not complete
        while i < len(L):
            l[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            l[k] = R[j]
            j += 1
            k += 1


if __name__ == "__main__":
    trial_size = 20
    values = []
    for i in range(trial_size):
        values.append(random.randint(0, trial_size))

    print(values)
    # bubble_sort(values)
    # selection_sort(values)
    # insertion_sort(values)
    merge_sort(values)
    print(values)