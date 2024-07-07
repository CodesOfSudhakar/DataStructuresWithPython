#Basic sequence types are LIST, TUPLE, Range etc...

stringVal = "This file is to practice about different sequence types in python"
wordList = list(stringVal.split(' ',maxsplit=7))

print(wordList)

for word in wordList:
    print(word)


#ENUMERATE
# Enumerate returns the index value while iterating. That index value must be captured in the code. Here it is indexVal in for statement.
# Eg below

for indexVal, word in enumerate(wordList):
    print("The current index is {0} and corresponding value is {1}".format(indexVal,word))

wordList2 = ["New", "list"]

#To combine 2 Lists, use EXTEND key word.

newList = wordList.extend(wordList2)

print(newList)