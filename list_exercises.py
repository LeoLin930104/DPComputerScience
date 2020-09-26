import random
import itertools
alist = [random.randint(0, 9) for i in range(10)]
blist = [random.randint(0, 9) for i in range(10)]

# 01. Sum all the elements of the list.
def find_sum(alist):
    print("Problem 1: Find Sum of Elements in list")
    print("Sum: {}".format(sum(alist)))

# 02. Write code that removes all the duplicates in a list.
def remove_duplicates(alist):
    print("Problem 2: Remove Duplicate in list")
    print("Reduced: {}".format(list(dict.fromkeys(alist))))

# 03. Write code that finds the similarities between two lists (Intersection)
def find_intersection(alist, blist):
    print("Problem 3: Find Intersection between lists")
    print("Intersection: {}".format([x for x in alist if x in blist]))

# 04. Write code that finds the differences between two lists.
def find_differences(alist, blist):
    print("Problem 4: Find differences between lists")
    print("Difference: {}".format([x for x in alist if x not in blist] + [x for x in blist if x not in alist]))

# 05. Write code that gets the frequency of items in a list.
def find_frequency(alist):
    print("Problem 5: Find frequency of elements in list")
    print("Frequency: {}".format(list(dict.fromkeys([(x, alist.count(x)) for x in alist]))))


if __name__ == "__main__":
    print("List A: {}".format(alist))
    print("List B: {}".format(blist))
    find_sum(alist)
    remove_duplicates(alist)
    find_intersection(alist, blist)
    find_differences(alist, blist)
    find_frequency(alist)
    