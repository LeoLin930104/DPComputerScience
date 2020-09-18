print("Hello World!")

# int
a = 3
atype = type(a)
print(a, atype)

# float
a = 7.77
atype = type(a)
print(a, atype)

# string
a = "string"
atype = type(a)
print(a, atype)

# back slash
a = 'I\'m a string'
atype = type(a)
print(a, atype)

# black text
a = """This is a very long string that can
go to a second line. Wow amazing."""
atype = type(a)
print(a, atype)

# type()
a, b = 2, "3"
atype, btype = type(a), type(b)
print(a, atype, b, btype)