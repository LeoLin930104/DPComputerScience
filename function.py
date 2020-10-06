def my_function():
    print("I'am a function")
my_function()

# width and height are parameters
def quad_area(width, height):
    return width * height

# When calling functions, width and height are arguements
area = quad_area(2,3)
print(area)

def nth_root(num: float, root: int, prec = 1e-20):
    if root < 0: return
    elif root % 2 == 0 and num < 0: return 0
    elif num == 0 or num == 1: return num

    g, prev = 1, 0
    while(abs(g - prev) > prec):
        prev = g
        g -= (g**root - num) / (root * g**(root - 1))
    return g

print(nth_root(25, 7))
print(nth_root(prec=0.001, root=7, num=25))