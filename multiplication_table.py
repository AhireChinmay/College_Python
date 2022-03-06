# Q- Write a program to print the multiplication number 
# of the entered number

a = int(input("Enter the number you want multiplication table of: "))
for i in range(10):
    print(f"{a}x{i+1}={a*(i+1)}")