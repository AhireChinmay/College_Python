# Lab Assignment no:18 : Create class EMPLOYEE for storing details 
# (Name, Designation, gender, Date of Joining and Salary). 
# Define function members to compute a)total number of employees in an
# organization b) count of male and female employee c) Employee with salary more than
# 10,000 d) Employee with designation “Asst Manager”.


class EMPLOYEE():
    def __init__(self, name,designation,gender,doJ,salary) :
        self.name = name
        self.designation = designation
        self.gender = gender
        self.doJ = doJ
        self.salary = salary

chinmay = EMPLOYEE()
chinmay.name = Chinmay
chinmay.designation = Manager
chinmay.gender = Male
chinmay.doJ = 12/3/2003
chinmay.salary = 12000000

print(chinmay())