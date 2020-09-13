#List are like a collection of data that can
#be accessed through a single variable
mylist = [1, 2, 3, 4, 5]
print(mylist, type(mylist))

print(mylist[0])
print(mylist[1])
print(mylist[2])
print(mylist[3])
print(mylist[4])

sum = 0
for num in mylist:
    print(num)
    sum += num
print(sum)

for i, x in enumerate(mylist):
    print("mylist:[{}] = {}".format(i, x))



