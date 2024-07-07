# Exploring about Numeric datatypes
import random

num1 = 5
num2 = 8

print(f"Addition operation of 2 numbers is {num1+num2}")

floatVal1 = -1.10
floatVal2 = 10.323

print(f"Sum of 2 decimal values is {floatVal1+floatVal2}")

#Using /, // and Modulo (%)

print(f" Using / operator {num1/num2}")
print(f" Using // operator {num1//num2}")
print(f" Using % operator {num1%num2}")

# // double slash discards the fractional part from the output displayed as shown in the o/p of line 16

# Powers of a number using ** Eg: 5**4 represents 5 powered 4

print(num1 ** num2)

## Common methods for numerical operations

listVar = [10123,234233,342,12,22324]

print(f"abs value of floatval1 is {abs(floatVal1)}")
print(f"rounded value of floatval2 is {round(floatVal2,3)}")
print(f"min value of the list is {min(listVar)}")
print(f"max value of the list is {max(listVar)}")
print(f"sum of list variables is {sum(listVar)}")
print(f"using pow and exponent {pow(num1,num2)}")

## Using some math functions by importing math class

import math

print(f"Factorial of a number --> {math.factorial(num1)}")
print(f"square root of a number --> {math.sqrt(num1)}")
print(f"Ceil of a number --> {math.ceil(floatVal1)}")
print(f"Floor of a number --> {math.floor(floatVal1)}")


## Generating random numbers

print(f"Generating random numbers -- {random.random()}")

## Generates a random int value between the given parameters including the given values
print(f"Generating random numbers -- {random.randint(num1,num2)}")

# Generates a random floating value inclusive of the given parameters
print(f"Generating random float value --> {random.uniform(floatVal1,floatVal2)}")