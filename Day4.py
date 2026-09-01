# Program 1
# num = 1
# while num <= 10:
#     print(num)
#     num = num + 1

# Program 2
# num = 1
# while num <= 10:
#     print(num, end = " ")
#     num = num + 1

# Program 3
# num = 1
# while num <= 20:
#     if ( num%2 ==0):
#         print(num)
#     num = num + 1

# Program 4
# num = 1
# while num <= 20:
#     if ( num%2 !=0):
#         print(num)
#     num = num + 1

# Program 5
# num = 1
# while num <= 50:
#     if ( num%5 ==0):
#         print(num)
#     num = num + 1

# Program 6
# num = int(input("Enter a number : "))
# a = 1
# while a <= num:
#     print(a)
#     a = a + 1

# Program 7 - Wasn't able to do this program
# passwd = input("Enter your password : ")
# while passwd != "Python123":
#     print("You have entered incorrect password")
#     passwd = input("Enter your password : ")
# print("You have entered correct password")

# Program 8
# num = 0
# while num < 20:
#     num = num + 1
#     if ( num%5 ==0):
#         continue
#     print(num)

# Mini Project
# pin = int(input("Enter your pin : "))
# count = 1
# while pin!= 123 and count<3:
#     print("Entered pin is incorrect, please try again " + "you have " + str(3-count) + " attempts left")
#     pin = int(input("Enter your pin : "))
#     count = count+1
# else :
#     if pin == 123:
#         print("Welcome! You have entered correct pin")
#     else:
#         print("You have entered incorrect pin 3 times, your account is blocked")  

# Program 9 - printing countdown of a number taken from user
# num = int(input("Enter a number : "))
# count = num
# while count > 0:
#     print(count)
#     count = count - 1

# Program 10 - sum until zero is entered
# sum = 0
# num = int(input("Enter a number : "))
# while num > 0:
#     sum = sum + num
#     num = int(input("Enter a number : "))

# print("The sum is :", sum)

# Program 11 - number guessing system with limited counts
# count = 1
# num = 15
# guess = int(input("Enter a number between 1 to 20 : "))
# while guess != num and count < 5:
#     print("You have guessed the wrong number " + "you have " + str(5-count) + " attempts left")
#     guess = int(input("Enter a number between 1 to 20 : "))
#     count = count + 1
# else:
#     if guess == num:
#         print("You have guessed the correct number")
#     else:
#         print("You have guessed the wrong number 5 times, you have lost the game")

# program 12 - number guessing with unlimited counts
# count = 1
# num = 15
# guess = int(input("Enter a number between 1 to 20 : "))
# while guess != num:
#     print("You have guessed the wrong number ")
#     guess = int(input("Enter a number between 1 to 20 : "))
#     count = count + 1
# else:
#     if guess == num:
#         print("You have guessed the correct number " + " and you took " + str(count) + " attempts to pass the game")
#     else:
#         print("You have lost the game")

# Program 13 - Sum of positive numbers only
# sum = 0
# num = int(input("Enter a number : "))
# while num > 0:
#     sum = sum + num
#     num = int(input("Enter a number : "))
#     if num < 0:
#         print("Negative numbers are ignored")
#         num = int(input("Enter a number : "))
#         continue
#     elif num == 0:
#         break
# print("The sum is :", sum)

# Program 14 - banking System
# balance = int(input("Enter your balance : "))
# choice = 1
# while choice <=4:
#     print("1 Deposit Money")
#     print("2 Withdraw Money")
#     print("3 check Balance")
#     print("4 Exit")
#     choice = int(input("Enter your choice : "))
#     if choice == 1:
#         deposit = int(input("Enter the money you want to deposit : "))
#         balance = balance + deposit
#     elif choice == 2:
#         withdraw = int(input("Enter the money you want to withdraw : "))
#         if withdraw > balance :
#             print("Insufficient balance" + " your balance is : " + str(balance))
#         else:
#             balance = int(balance - withdraw)
#     elif choice == 3:
#         print("Your balance is : " + str(balance))
#     elif choice == 4:
#         print("Thank you for using our banking system")
#         break   

# # Program 15 - finding largest number from user input until -1 is entered
# num = int(input("Enter a number : "))
# l_num = 0
# while num != -1:
#     if num > l_num:
#         l_num = num
#         num = int(input("Enter a number : "))
#     else:
#         num = int(input("Enter a number : "))
# print("The largest number is : " , str(l_num))

# Program 16 - pattern style problem
# row = 1
# num = int(input("Enter a number : "))
# while row<=num:
#     col = 1
#     while col <= row:
#         print(col, end = " ")
#         col = col+1
#     print()

#     row = row + 1

# Program 17 - pattern style problem
# row = 1
# num = int(input("Enter a number : "))
# while row<=num:
#     col = 1
#     while col <= row:
#         print(row, end = "")
#         col = col+1
#     print()

#     row = row + 1

# Program 18 - pattern style problem
# row = 1
# num = int(input("Enter a number : "))
# while row<=num:
#     col = 1
#     while col <= num:
#         print(row, end = "")
#         col = col+1
#     print()

#     row = row + 1

# Program 19 - pattern style problem

# row = 1
# count = 1
# while row<=3:
#     col = 1
#     while col <= 3:
#         print(count, end = "")
#         count = count + 1
#         col = col + 1
#     print()
#     row = row + 1
    

        

    


    

