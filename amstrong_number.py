# To check whether input number is Armstrong number or not. An Armstrong 
# number is an integer with three digits such that the sum of the cubes of
# its digits is equal to the number itself. Ex. 371.

num = int(input("Enter a number: "))

sum = 0

temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3

if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")
