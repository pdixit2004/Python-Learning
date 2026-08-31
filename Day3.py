# Program 1
# age = int(input("Enter your age : "))
# if  (age >= 18):
#     print("You are eligible to vote")
# else:
#     print("You are not eligible to vote")

# Program 2
# marks = int(input("Enter your marks : " ))
# if (marks >=40):
#     print("You are pass")
# else:
#     print("You are fail")

# Program 3
# a = int(input("Enter a number : "))
# if (a>0):
#     print("Number is positive")
# elif (a<0):
#     print("Number is negative")
# else:
#     print("Entered number is zero")

# Program 4
# salary = int(input("Enter your salary : "))
# if (salary > 100000):
#     print("You have a high income")
# else:
#     print("Your income is low")

# Program 5
# username = input("Enter your username : ")
# if (username == 'prakhar'):
#     print("Welcome " , username )
# else:
#     print("You are not authorized to access this system")

# Program 6
# age = int(input("Enter your age : "))
# citizenship = input("Enter your citizenship : ")
# if (age>=18 and citizenship.lower() == 'indian'):
#     print("You are eligible to vote")
# else:
#     print("You are not eligible to vote")

# Program 7
# marks = int(input("Enter your marks : "))
# if (marks >90):
#     print("You have scored Grade A")
# elif(marks>75):
#     print("You have scored Grade B")
# elif (marks > 60):
#     print("You have scored Grade C")
# elif(marks>40):
#     print("You have scored Grade D")
# else:
#     print("You are failed and scored Grade F")

# Mini-Project
name = input("Enter your name : ")
r_num = input("Enter your roll number : ")
p1 = int(input("Enter marks of Physics : "))
p2 = int(input("Enter marks of Chemisty : "))
p3 = int(input("Enter marks of Maths : "))
average = float(round((p1 + p2 + p3) / 3 , 3))
print(" STUDENT REPORT")
print("Name : ", name)
print("Roll Number : ", r_num)
print("Average Marks : ", average)
if (average >90):
    print("You have scored Grade A")
elif(average>75):
    print("You have scored Grade B")
elif (average > 60):
    print("You have scored Grade C")
elif(average>40):
    print("You have scored Grade D")
else:
    print("You are failed and scored Grade F")
