#Using Separators/End Argument inside the print statement


print('hello world')

name = "Sudhakar"
print(name)

folderPath = r"c:\filepath\filename.extension"
print(folderPath)

namewithSingleQ = r"This is Sudhakar's folder"
namewithDoubleQ = r'This is "Python" learning folder'

print("Printing Line 1: {0} \n"
      "Printing Line 2: {1}".format(namewithSingleQ,namewithDoubleQ)
      )

## Using F-Strings

print('\n Using F-STRINGS for python formatting. This is the latest version instead of using .format method \n')
print(f"This is my name- {name} and these are the variable 1-{namewithSingleQ} and variable 2-{namewithDoubleQ}")


#Print statement arguments --- END

listVariable = [1, 2, 3, 4, 5]

for i in listVariable:
    print(i,end='---')

print("End of for loop")

#To enumerate

for index, i in enumerate(listVariable):
    if index==(len(listVariable)-1):
        print(i)
    else:
        print(i,end='---')
print("End of for loop with Enum")

#Unpacking iterables in Print statement.

print("\n Unpacking a List")

print(*listVariable, sep='---')



#Using FLUSH parameter -- This is used to explicity force the Python to print the value to the console immediately
#when set to TRUE. Otherwise python will internally decide when to print it., For example. While printing a list
#it will print everything at the end of final iteration ...

for i in listVariable:
    print(i,end='\n',flush=False)