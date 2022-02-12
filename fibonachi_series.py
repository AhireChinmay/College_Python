num= int(input("Enter how many numbers you want fabonacci series of : "))
a= 0
b= 1
series = 0
MyList = []
for i in range(num):
    MyList.append(series)
    a = b
    b = series
    series = a+b

print(MyList)