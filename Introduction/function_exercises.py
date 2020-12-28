import copy

# Write a function that calculates a factorial
# factorial(5) -> 120
# factorial(7) -> 5040
# factorial(10) -> 3628800
def factorial(n: int) -> int:
    result = 1
    for x in range(n, 1, -1):
        result *= x
    return result


def factorial_rec(n: int) -> int:
    if n == 1:
        return 1
    else:
        return factorial_rec(n - 1)


# Write a function that calculates a permutation
# n! / (n-r)!
# nPr(10, 10) -> 3628800
# nPr(10, 7) -> 604800
# nPr(10, 4) -> 5040
def nPr(n: int, r: int) -> int:
    return int(factorial(n) / factorial(n - r))


# Write a function that calculates a combination
# n! / (r!(n-r)!)
# nCr(10, 10) -> 1
# nCr(10, 7) -> 120
# nCr(10, 4) -> 210
def nCr(n: int, r: int) -> int:
    return int(factorial(n) / (factorial(r) * factorial(n - r)))


# Write a function that returns a list of n rows of Pascal's Triangle
# pascals_triangle(3) -> [[1], [1, 1], [1, 2, 1]]
# pascals_triangle(6) -> [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]]
# pascals_triangle(9) -> [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1], [1, 6, 15, 20, 15, 6, 1], [1, 7, 21, 35, 35, 21, 7, 1], [1, 8, 28, 56, 70, 56, 28, 8, 1]]
def pascals_triangle(n: int) -> list:
    pascal = [1]
    for _ in range(n):
        temp = copy.copy(pascal)
        temp.insert(0, 0)
        for i, x in enumerate(pascal):
            pascal[i] += temp[i]
        pascal.append(1)
    return pascal


def pascal_triangle_brent_1(n: int) -> list:
    pascal = []
    for i in range(n):
        pascal = []
        for r in range(i + 1):
            term = nCr(i, r)
            pascal.append(term)
        pascal.append(pascal)
    return pascal


def pascal_triangle_brent_2(n: int) -> list:
    prev, new, rows = [1], [1], []
    for r in range(n):
        new = [1] + [
            prev[i] + prev[i + 1] for i, _ in enumerate(prev) if i < len(prev) - 1
        ]
        if r > 0:
            new.append(1)
        rows.append(new)
        prev = new
    return rows


# Write a generator that produces a string of * characters, each line one * longer than the previous
# gen = star_gen()
# next(gen) -> *
# next(gen) -> **
# next(gen) -> ***
# next(gen) -> ****
# next(gen) -> *****
def star() -> str:
    star = ""
    while True:
        star += "*"
        yield star


# Seive of eratosthenes
# Create a generator function that will return the next prime number using
# the seive of eratosthenes
# gen = prime()
# next(gen) -> 2
# next(gen) -> 3
# next(gen) -> 5
# next(gen) -> 7
# next(gen) -> 11
def divisible(prime: list, current: int) -> bool:
    for x in prime:
        if current % x == 0:
            return True


def next_prime() -> int:
    prime = [2]
    current = 2
    while True:
        current += 1
        if divisible(prime, current):
            continue
        else:
            prime.append(current)
            yield current


# Write a generator function that returns the next row of
# Pascal's Triangle each time it is called
# gen = pascals_triangle_gen()
# next(gen) -> [1]
# next(gen) -> [1, 1]
# next(gen) -> [1, 2, 1]
# next(gen) -> [1, 3, 3, 1]
# next(gen) -> [1, 4, 6, 4, 1]
def pascals_triangle_gen() -> list:
    n = 1
    while True:
        yield pascals_triangle(n)
        n += 1


def pascals_triangle_gen_brent() -> list:
    prev, new = [1], [1]
    while True:
        yield new
        new = (
            [1]
            + [prev[i] + prev[i + 1] for i, _ in enumerate(prev) if i < len(prev) - 1]
            + [1]
        )
        prev = new


# Execute Tests
print("Factorial")
print(factorial(5))

print("Permutation")
print(nPr(10, 10))

print("Combination")
print(nCr(10, 4))

print("Star")
gen = star()
for _ in range(10):
    print(next(gen))

print("Pascal Triangle")
print(pascals_triangle(3))

print("Prime")
gen = next_prime()
for _ in range(1000):
    print(next(gen))

print("Pascal Triangle Generator")
gen = pascals_triangle_gen_brent()
for _ in range(10):
    print(next(gen))
