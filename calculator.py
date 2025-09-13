# calculator app
import math

print("Welcome to the Calculator App!")
print(" " )
para="""
Addition: +
Subtraction: -
Multiplication: *
Division: /
Floor Division: //
Modulus: %
Exponentiation: **
"""
print (para)

operator=input("Select operation +,-,*,/,// :")
num1=float(input("enter num 1:"))
num2=float(input("enter num 2:"))

if operator=='+':
    print((num1+num2))
elif operator=='-':
    print((num1-num2))
elif operator=='*':
    print((num1*num2))
elif operator=='/':
    print((num1/num2))
elif operator=='//':
    print((num1 //num2))
elif operator=='**':
    print((num1**num2))
elif operator=='+':
    print((num1+num2))
elif operator=='%':
    print((num1%num2))
else:
    print("give valid output")



