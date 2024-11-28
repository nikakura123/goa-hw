for i in range(0, 20, 2):
    print(i)
number =  7
user_guess = int(input("pick a number 1-10"))
while  user_guess != number:
    int(input("pick a number 1-10"))
if user_guess == number:
    print("you guess the number")
password = 123
user_password = int(input("enter password"))
while user_password != password:
    int(input("enter password"))
if user_password == password:
    print("Password is correct")