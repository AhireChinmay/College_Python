# Q - Write a programme to convert temperature from Celsius to Farenheit 
#     and vise versa

a = input("Enter 'f' for farenheit or 'c' for celcius: ")
temp = int(input("Enter the temperature: "))
f = (temp*1.8)+32
c = (temp-32)*5/9
if a =='c':
    print("celsius to farenheit is: ",f,"F")
elif a =='f':
    print("farenheit to celsius  is: ",c,"°C")

