# Newton's Method
# Find Initial Guess
# For many Iterations
# guess = f(guess) / f'(guess)


def newton(a, b, c):
    g = (b ** 2 - 4 * a * c) + 100
    for i in range(100):
        g -= (a * g ** 2 + b * g + c) / (2 * g + b)
        print(g)
    print("Root: {}".format(g))


if __name__ == "__main__":
    a = int(input("a: "))
    b = int(input("b: "))
    c = int(input("c: "))
    newton(a, b, c)