# Q- Write a program to find whether a person is passed or failed when 
# he enters his marks of 5 subjects

S1_marks = int(input("Enter marks of first subject: "))
S2_marks = int(input("Enter marks of second subject: "))
S3_marks = int(input("Enter marks of third subject: "))
S4_marks = int(input("Enter marks of forth subject: "))
S5_marks = int(input("Enter marks of fifth subject: "))


overall_percentage = (S1_marks+S2_marks+S3_marks+S4_marks+S5_marks)/5
print("Your Overall Percentage is :",overall_percentage,"%")

if (S1_marks>40) and (S2_marks>40) and (S3_marks>40)and (S4_marks>40) and (S5_marks>40) and (50>overall_percentage>=40):
    print("You are pass with 3rd division")
elif (S1_marks>40) and (S2_marks>40) and (S3_marks>40)and (S4_marks>40) and (S5_marks>40) and (60>overall_percentage>=50):
    print("You are pass with 2nd division")
elif (S1_marks>40) and (S2_marks>40) and (S3_marks>40)and (S4_marks>40) and (S5_marks>40) and (75>overall_percentage>=60):
    print("You are pass with first division")
elif (S1_marks>40) and (S2_marks>40) and (S3_marks>40)and (S4_marks>40) and (S5_marks>40) and (overall_percentage>=75):
    print("You are pass with distinction")
else:
    print("You is fail as hell")

