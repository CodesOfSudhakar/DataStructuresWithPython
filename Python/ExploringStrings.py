strVar1 = "Hello world"
strVar2 = "HELLO WORLD"
strVar3 = "hello world"

print(strVar1.upper())
print(strVar2.lower())
print(strVar3.capitalize())  #Capitalizes the first letter of each word
print(strVar1.replace("world","Sudhakar"))

#Finding a letter in a string

print(strVar1.find("or"))
print(strVar1.index("or"))


# Find and Index are used for the same purpose. But the Find returns -1 when the substring is not found
# in the given string. Whereas Index returns an error value in case the substring is not found.
# This makes .find more preferable over the Index. No need of additional error handling required for Find method

strVar4 = " ".join([strVar1,strVar2,strVar3])

print(strVar4.lower().count("hello")) # Counting total occurence of a string



