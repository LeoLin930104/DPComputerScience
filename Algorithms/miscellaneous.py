import random


def min_difference_neighbor(l: list) -> (int, int, int):
    min = abs(l[0] - l[1])
    neighbor1 = 0
    neighbor2 = 0
    for i in range(len(l) - 1):
        if abs(l[i] - l[i + 1]) < min:
            min = abs(l[i] - l[i + 1])
            neighbor1 = i
            neighbor2 = i + 1
    return (min, neighbor1, neighbor2)


if __name__ == "__main__":
    values = [5, 1, 4, 7, 9, -12]
    trial_size = 20
    values = []
    for i in range(trial_size):
        values.append(random.randint(0, trial_size))
    result = min_difference_neighbor(values)
    print(
        f"Values: {values} \nMinimum Difference is {result[0]} between element {result[1]} and {result[2]}"
    )
