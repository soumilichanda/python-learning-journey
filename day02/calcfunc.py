def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if b == 0:
        return"Cannot divide by zero"
    return a/b
try:
 num1 = float(input("Enter 1st number : "))
 num2 = float(input("Enter 2nd number : "))

 sum = add(num1,num2)
 print(sum)
 diff = subtract(num1,num2)
 print(diff)
 product = multiply(num1,num2)
 print(product)
 div = divide(num1,num2)
 print(div)
except ValueError:
 print("\nInvalid Input")