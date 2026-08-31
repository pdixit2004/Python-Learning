# #Program 1
# a = input("Enter first number : ")
# b = input("Enter second number : ")
# print("Sum of numbers is : " + str(int(a) + int(b)))
# print("Difference of numbers is : " + str(int(a) - int(b)))
# print("Product of numbers is : " + str(int(a) * int(b)))
# print("Division of numbers is : " + str(round(int(a) / int(b), 2)))
# print("Floor Division of Numbers is : " + str(int(a) // int(b)))
# print("Modulus of numbers is : " + str(int(a) % int(b)))
# print("Exponent of numbers is : " + str(int(a) ** int(b)))

# #Program 2
# age = int(input("Enter your age : "))
# print("Is age greater than 18 : " , age > 18)

# Program 3
# a = input("Enter first number : ")
# b = input("Enter second number : ")
# if int(a) > int(b):
#     print(a)
# else:
#     print(b)

# Program 4
# a = input("Enter number : ")
# if int(a) % 2 == 0:
#     print("The entered number is even")
# else:
#     print("The entered number is odd")

# Program 5
# a = int(input("Enter a number : "))
# b = int(a ** 2)
# c = int(a ** 3)
# print("The square of entered number is : ", b)
# print("The cube of entered number is : ", c)

# Mini-Project
name = input("Enter your name : ")
monthly_salary = int(input("Enter your monthly salary : "))
bonus = int(input("Enter your bonus : "))
tax = int(input("Enter your tax : "))
final_salary = str(int((monthly_salary + bonus) - tax))
print("Employee Name is : " + name + " & Final Salary is : " + final_salary)