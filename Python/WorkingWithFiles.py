# sampleFile = open('FileInput.txt','r')
#
# for eachLine in sampleFile:
#     lineLength = len(eachLine.strip())
#
#     if lineLength!=0:
#         print(eachLine,end='-')


with open('FileInput.txt', 'r') as inputFile:

    for eachLine in inputFile:
        lineLength = len(eachLine.strip())
        if lineLength != 0:
            print(eachLine, end='')







