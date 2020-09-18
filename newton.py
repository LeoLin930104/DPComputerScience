# Newton's Method
# Find Initial Guess 
# For many Iterations
# guess = f(guess) / f'(guess)

def newton():
    g = 1
    for i in range(100):
        g -= (g**2 - 8*g + 18) / (2*g - 8)
    print(g)

if __name__ == "__main__":
    newton()