print("Hello World!")

a = 3
atype = type(a)
print(a, atype)

a = 7.77
atype = type(a)
print(a, atype)

a = "string"
atype = type(a)
print(a, atype)

a = 'I\'m a string'
atype = type(a)
print(a, atype)

a = """This is a very long string that can
go to a second line. Wow amazing."""
atype = type(a)
print(a, atype)

a, b = 2, "3"
atype, btype = type(a), type(b)
print(a, atype, b, btype)