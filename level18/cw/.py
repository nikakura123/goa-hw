number = int(input("enter number"))

if  number % 2 == 0:
     print("the number is even")
else:
     print("the number is odd")

age = int(input("select your age"))
if age <= 18:
     print("you can not vote")
else:
     print("you can vote")


password =int("1122")
user_password = int(input("enter password"))


if user_password == password:
     print("access granted")
else:
     print("access  denied")