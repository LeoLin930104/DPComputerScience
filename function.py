# Function only do one thing
# Function has a input and a output
# Function has pre-conditions and post-conditions 

def my_function():
    print("I'am a function")
my_function()

# width and height are parameters
def quad_area(width, height):
    return width * height

# When calling functions, width and height are arguements
area = quad_area(2,3)
print(area)

# Find the nth root of a number
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

def change1(mylist: list):
    mylist.append([4,5,6])
    # print("List in Change1: {}".format(mylist))
    print(f"List in Change1: {mylist}")

def change2(mylist: list):
    mylist = [4,5,6]
    # print("List in Change2: {}".format(mylist))
    print(f"List in Change2: {mylist}")

# All parameters are pass-by-reference
mylist = [1,2,3]
print(f"Before Change1: {mylist}")
change1(mylist)
print(f"After Change1: {mylist}")

print()

print(f"Before Change2: {mylist}")
change2(mylist)
print(f"After Change2: {mylist}") 

# Function can be nested inside other functions
def nth_root2(num: float, root: int, prec=1e-20):
    if root < 0: return
    elif root % 2 == 0 and num < 0: return 0
    elif num == 0 or num == 1: return num

    g = 1
    prev = 0

    def f(num: float, root: int, g: float) -> float:
        return g**root - num
    def df(root: int, g: float) -> float:
        return root * g**(root-1)
        
    while(abs(g - prev)> prec):
        prev = g
        g -= f(num,root,g) / df(root,g)
    
    return g

print(nth_root2(50,4))

nth_root3 = nth_root2
print(nth_root3(50, 4))

def even(val: int):
    print(f"{val} is an even number")

def odd(val: int):
    print(f"{val} is an odd number")

def do_a_thing(even_callback: callable, odd_callback: callable):
    for i in range(20):
        if i % 2:
            odd_callback(i)
        else:
            even_callback(i)

do_a_thing(even, odd)

# Generator Functions
# Yeild(return) without terminating the function
def squares() -> int:
    n = 1
    while True:
        yield n**2
        n+=1

gen = squares()
val = next(gen)
print(val)
val = next(gen)
print(val)

# Different Pointer creates separate Increament in Squares()
gen2 = squares()
val = next(gen2)
print(val)

def fibonacci():
    x, y = 0, 1
    while(True):
        x, y = y, x + y
        yield x

# Fibonacci Function by Generator
gen = fibonacci()
for _ in range(20):
    print(next(gen))

# Code of the Range Function
def range(end: int , start: int = 0, step: int = 1) -> int:
    if step == 0:
        return
    elif step > 0:    
        while start < end:
            yield start
            start = start + step
    else:
        while end > start:
            yield start
            start = start + step

for n in range(10):
    print(n)
