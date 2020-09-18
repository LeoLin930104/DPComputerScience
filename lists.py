#List are like a collection of data that can
#be accessed through a single variable
mylist = [1, 2, 3, 4, 5]
print(mylist, type(mylist))

# asign values 
print(mylist[0])
print(mylist[1])
print(mylist[2])
print(mylist[3])
print(mylist[4])

# printing lists with loops
sum = 0
for num in mylist:
    print(num)
    sum += num
print(sum)

for i, x in enumerate(mylist):
    print("mylist:[{}] = {}".format(i, x))

# insert element
mylist.append(6)
mylist.append([1,2,3,4])
mylist.extend([5,6,7,8])
print(mylist)

# insert element with different types
mylist = [1, 2.0 , "3", [4, 5], [6, "7", 8]]
mylist[4][2] = 9.0
print(mylist)

# length of list
length = len(mylist)
print(length)

# Repeated elements asign
mylist = [0]*20
print(mylist)
mylist = [0,1]*10
print(mylist)

# Statements
mylist = ['a', 'b', 'c', 'd', 'c', 'a']
exist = 'c' in mylist
print(exist)
print('c' not in mylist)

# Index, find location
location = mylist.index('c')
print(location)
location = mylist.index('c', 3)

# Insert/Remove element by Index
mylist.insert(3, 'z')
print(mylist)
mylist.remove('b')
print(mylist)

# Pop/Push
val = mylist.pop()
print(val, mylist)
val = mylist.pop(3)
print(val, mylist)

# Count
count = mylist.count('c')
print(count)

# Sort
mylist.sort()
print(mylist)
mylist.sort(reverse = True)
print(mylist)

# List from 1 to 10
for i in range(1,11):
    mylist.append(i)
print(mylist)

mylist = [i for i in range(1, 11)]
print(mylist)
mylist = [i for i in range(2, 22, 2)]
print(mylist)
mylist = [i*2 for i in range(1, 11)]
print(mylist)
mylist = [i for i in range(1,21) if i % 2 == 0]
print(mylist)
mylist = [i for i in range(1, 11)]

# Filter
filtered = [i for i in mylist if i > 5]
print(filtered)

filtered = [i**3 for i in mylist]
print(filtered)

# Sublist: first inclusive, end exclusive
mylist = [i for i in range(0, 20)]
sublist = mylist[3:10]
print(sublist)
sublist = mylist[3:10:2]
print(sublist)
sublist = mylist[3:]
print(sublist)
sublist = mylist[:10]
print(sublist)
sublist = mylist[::2]
print(mylist)

# Swap Element
a = 1
b = 2
[a, b] = [b, a]
print(a, b)

# Shallow Copy
mylist = [i for i in range(5)]
newlist = mylist
newlist[0] = 100
print(mylist, newlist)