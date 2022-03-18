# To accept the number and Compute 
# a) square root of number
# b) Square of number
# c)Cube of number 
# d) check for prime
# e) factorial of number 
# f) prime factors
import math

def square_root(a):
    return math.sqrt(a)
def square (a):
    return a**2
def cube (a):
    return a**3
def isPrime(a):
    if a <= 1:
        return False
  
    for i in range(2, a):
        if a % i == 0:
            return False;
    return True
def factorial(a):
    for i in range(1,a):
        a*=i
    return a 
def prime_factors(a):
    for i in range(2,a+1):
        if a%i==0:
            prime = True
            for j in range(2,i//2+1):
                if i%j==0:
                    prime = False
                    break
            if prime:
                print ("%d"%i,end=" ")
    print(f"are the prime factors of {a}")

num = int(input("Enter the number you want to do operations on: "))
take = input('''Enter a) square root of number
b) Square of number
c)Cube of number 
d) check for prime
e) factorial of number 
f) prime factors\n''')
 
if take == 'a':
    print("The square root of number is",square_root(num))
if take == 'b':
    print("The square of number is",square(num))
if take == 'c':
    print("The cube of number is",cube(num))
if take == 'd':
    print("This is a prime number") if isPrime(num) else print("Not a prime number")
if take == 'e':
    print("The factorial of number is",factorial(num))
if take == 'f':
    print(prime_factors(num))

                


