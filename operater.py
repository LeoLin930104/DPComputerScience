# Operations between Different types, Casting
print("Hello World!")

a, b = 2, 3
result = a + b
print("{} + {} = {}".format(a, b, result))
print("{} + {} = {}".format(type(a), type(b), type(result)))

a, b = 1.7, 4.6
result = a + b
print("{} + {} = {}".format(a, b, result))
print("{} + {} = {}".format(type(a), type(b), type(result)))

a, b = 1.7, 4
result = a + b
print("{} + {} = {}".format(a, b, result))
print("{} + {} = {}".format(type(a), type(b), type(result)))

a, b = "number: ", 4
result = a + str(b)
print("{} + {} = {}".format(a, b, result))
print("{} + {} = {}".format(type(a), type(b), type(result)))

a, b = 6, "4"
result = a + int(b)
print("{} + {} = {}".format(a, b,  result))
print("{} + {} = {}".format(type(a), type(b), type(result)))