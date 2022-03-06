# Q- Write a program to find the maximum and 
# minimum of a list entered by user 

n = int(input("Enter the size of for loop: "))
MyList=[]
for i in range(1,n+1):
   num = int(input("Enter the numbers: "))
   MyList.append(num)
print("The Minimum is :",min(MyList))
print("The Maximum is :",max(MyList))
print("The Sum is :",sum(MyList))
print("The Average is :",sum(MyList)/n)