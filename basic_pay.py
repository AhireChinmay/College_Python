basic_pay = int(input("Enter your income in Rs: "))
hra = (10/100)*basic_pay
ta = (5/100)*basic_pay
total_income = basic_pay-hra-ta
tax = (2/100)*total_income
net_income = total_income-tax
print("Your HRA is",hra,"Rs")
print("Your TA is",ta,"Rs")
print("Your total income is",total_income,"Rs")
print("Total tax to be paid is ",tax)
print("Your net income is",net_income,"Rs")