
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

#Print statement arguments --- END

list = [1,2,3,4,5]

for i in list:
    print(i,end='---')

print("End of for loop")

#To enumerate

for index, i in enumerate(list):
    if index==(len(list)-1):
        print(i)
    else:
        print(i,end='---')
print("End of for loop with Enum")