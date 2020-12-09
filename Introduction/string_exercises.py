# 01. Write a program to count and return a dictionary of character frequencies in a given string
def frequency():
    mydict = {}
    mystr = input("Insert a string: ")
    mylist = [x for x in mystr]
    for x in mylist:
        if x not in mydict:
            mydict[x] = mylist.count(x)
    print(mydict)
# 02. Write a program to insert a string in the middle of a string
def insertStr(): 
    mystr1 = input("Insert a string of even length: ")
    mystr2 = input("Insert another string: ")
    print(mystr1[:len(mystr1)//2] + mystr2 + mystr1[len(mystr1)//2:])

# 03. Write a program to display a number with comma seperators
def seperator():
    mydict = {"ch" : (4, ','), "en" : (3, ','), "fr" : (3, '.')}
    mystr = input("Insert a number string: ")
    myType = input("Insert type of translation (ch, en, fr): ")
    mylist = [x for x in mystr]
    if mystr.isnumeric() == False:
        print("String Not Numeric")
        return
    elif myType not in mydict:
        print("Type Not Recognized")
        return
    else:
        mySyn = mydict.get(myType)
        
    myNew = ""
    for i in range(len(mystr)-mySyn[0], 0, -(mySyn[0])):
        mystr = mystr[:i] + mySyn[1] + mystr[i:]
    print(mystr)
    
# 04. Write a program to move the spaces to the from of a given string
def moveSpace():
    mystr = input("Insert a string: ")
    mylist = mystr.split(' ')
    mynew = " " * (len(mylist)-1)
    for x in mylist: mynew += x
    print(mynew)
# 05. Write a program to compute the sum of the digits of a sum of a given numeric string
def sumString():
    mystr = input("Insert a number string: ")
    if mystr.isnumeric() == True : print(sum([int(x) for x in mystr]))
    else : print("String Not Numeric") 
    
# 06. Write a program to determine if a set of parenthesis are balanced
def balanceParen():
    myParen = input("Insert a string with only parenthesis: ")
    if myParen.count('(') + myParen.count(')') != len(myParen):
        print("Include character else than parenthesis")
        return
    current = 0
    balance = True
    for x in myParen:
        if current < 0: balance = False
        else:
            if   x == '(': current += 1
            elif x == ')': current -= 1
    if current != 0: balance = False
    print(balance)

if __name__ == "__main__":
    frequency()
    insertStr()
    seperator()
    moveSpace()
    sumString()
    balanceParen()
    pass
