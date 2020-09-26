# Basic Strings
text = 'This is a string'
text = "This is a string"
text = """This is a string"""
print(text)

text = 'This is a string with "double quoate"'
text = "This isn't a string with double quote"
text = """This isn't a string with a "double quote" """

# Special Characters (escape characters)
text = "\' \" \\ are \t escape \n character"
print(text)

# Raw Text
text = r"This is raw text. \r \t \n \\ \" do nothing"
print(text)

# String Resoruces of System
import sys
print(sys.getdefaultencoding())

# Using unicode to Call for Character
text = "The circumfrence of a circle is 2\u03c0r"
print(text)

text = "我會寫中文"
text = "\u6211\u6703\u5BEB\u4E2D\u6587"
print(text)

# Iterating using String
text = "This is a string"
for c in text:
    print(c)
text = "This is just a longer string that we are going to code with"

substring = text[10:]
print(substring)
substring = text[:10]
print(substring)
substring = text[5:20]
print(substring)

text = "42"
num = text.isdigit()
print(num)
letter = text.isalpha()
print(letter)
letOrNum = text.isalnum()
print(letOrNum)
length = len(text)
print(length)

text = "This is just a longer string that we are going to code with"
print(text.upper())
print(text.lower())
print(text.title())
print(text.swapcase())
print(text.capitalize())

# Formating 
print(text.center(100))
print(text.ljust(100))
print(text.rjust(100))

# Replacing
print(text.replace('th', 'zz'))
print(text.replace('th', 'zz', 1))

# Spliting 
print(text.split(' '))

# Finding
print(text.startswith('This'))
print(text.endswith('This'))
print(text.find('th'))
print(text.find('th', 20))
print(text.rfind('th', 20))
print(text.index('th'))
# ----print(text.index('xw'))

# Join Lists into String
words = ['one', 'two', 'three', 'four']
text = ' '.join(words)
print(text)
