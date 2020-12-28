# Dictionary in Python
mydict = {"givenName": "Leo", "familyName": "Lin", "Age": "16"}
print(mydict)

givenName = mydict["givenName"]
print(givenName)

dictItems = mydict.items()
print(dictItems)

# Keys and Values
for key, value in mydict.items():
    print("{}: {}".format(key, value))

for key in mydict.keys():
    print(key)

age = mydict.get("age")
print(age)

# Determine if a key exist in a dictionary
haskey = "familyName" in mydict
print(haskey)

# Null Return in Dictionary
something = mydict.get("DNE")
print(something)
# Not always safe
# ----something = mydict['DNE']
# ----print(something)

# Remove Data with Keys and Return
familyName = mydict.pop("familyName", 'There isn\'t "familyName"')
print(familyName)
print(mydict)

del mydict["Age"]
print(mydict)

something = mydict.popitem()
print(something)
print(mydict)


# Emptying the Entire Dictionary
mydict.clear()
print(mydict)

# Add a new key
mydict = {}
mydict["one"] = 1
mydict["two"] = 2
mydict["three"] = 3
mydict["four"] = 4
mydict["one"] = 5
print(mydict)
