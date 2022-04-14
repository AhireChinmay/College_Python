# Lab Assignment no:18 : Create class EMPLOYEE for storing details 
# (Name, Designation, gender, Date of Joining and Salary). 
# Define function members to compute a)total number of employees in an
# organization b) count of male and female employee c) Employee with salary more than
# 10,000 d) Employee with designation “Asst Manager”.


class EMPLOYEE():
    count = 0
    female_count = 0
    male_count = 0
    salary_count = 0
    designation_count = 0
    def __init__(self, name,designation,gender,doJ,salary) :
        self.name = name
        self.designation = designation
        self.gender = gender
        self.doJ = doJ
        self.salary = salary
        
        if self.gender == "Male":
            EMPLOYEE.male_count += 1
            EMPLOYEE.count +=1
        if self.gender == "Female":
            EMPLOYEE.female_count +=1
            EMPLOYEE.count +=1
        if self.salary>10000:
            EMPLOYEE.salary_count += 1
        if self.designation == "Assistant Manager":
            EMPLOYEE.designation_count += 1
         
    
    def count_of_employee(self):
        print(f"The total no of empoloyees in this company are {self.count}")
    def count_of_males_females(self):
        print(f"The no of male employees are {self.male_count} and female employees are {self.female_count}")
    def count_of_salary(self):
        print(f"The employees with salary more than 10000 are {self.salary_count}")
    def count_AssnManager(self):
        print(f"The count of Assistant Managers in company is {self.designation_count}")
    def EmpDetails (self):
        print(f"Name of Employee is {self.name}")
        print(f"Designation of Employee is {self.designation}")
        print(f"Date of joining of Employee is {self.doJ}")
        print(f"Salary of Employee is {self.salary}\n")
        
employee1 = EMPLOYEE("Chinmay","CEO","Male","10/10/10",1000000)
employee2 = EMPLOYEE("Johny","Scum Master","Male","12/5/20",100000)
employee3 = EMPLOYEE("Priyanka","Senior Software Developer","Female","15/2/12",150000)
employee4 = EMPLOYEE("Steve","Programmer","Male","4/5/21",9000)
employee5 = EMPLOYEE("Amanda","Programmer","Female","14/5/16",70000)
employee6 = EMPLOYEE("Pranita","Assistant Manager","Female","18/3/15",90000)

employee6.count_of_employee()
employee6.count_of_males_females()
employee6.count_of_salary()
employee6.count_AssnManager()
print("\n The Employees are as follows \n")
employee1.EmpDetails()
employee2.EmpDetails()
employee3.EmpDetails()
employee4.EmpDetails()
employee5.EmpDetails()
employee6.EmpDetails()
