#Q -  To simulate simple calculator that performs basic tasks such as addition, 
#     subtraction, multiplication and division with special operations like 
#     computing xy and x!.

class calculator():
    def factorial(a,fact,i):    
        for i in range(1,a):
            fact += fact*i
        return fact
    def addition(a,b):
        return a+b
    def subtraction(a,b):
        return a-b
    def multiplication(a,b):
        return a*b
    def division(a,b):
        return a/b
    def power(a,b):
        return a**b    
i = 0
fact = 1
enter = input("Enter which calculation do you want to perform: ")

if enter == "F":
    a = int(input("Enter the number you want factorial of: "))
    print(calculator.factorial(a,fact,i))
if enter == "A":
    a = int(input("Enter the first number: ")) 
    b = int(input("Enter the second number: "))
    print(calculator.addition(a,b))
if enter == "S":
    a = int(input("Enter the first number: ")) 
    b = int(input("Enter the second number: "))
    print(calculator.subtraction(a,b))
if enter == "M":
    a = int(input("Enter the first number: ")) 
    b = int(input("Enter the second number: "))
    print(calculator.multiplication(a,b))
if enter == "D" :
    a = int(input("Enter the first number: ")) 
    b = int(input("Enter the second number: "))
    print(calculator.division(a,b))
if enter == "P":
    a = int(input("Enter the number: "))
    b = int(input("Enter the power: "))
    print(calculator.power(a,b))