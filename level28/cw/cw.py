# # Sum of Two Numbers
# # Write a function add_numbers(a, b) that takes two numbers and returns their sum.

# def add_numbers(a, b):
#   return a + b

# print(add_numbers(2,4))

# # Check Even or Odd
# # Write a function is_even(number) that returns True if a number is even, otherwise False.

# def is_even(a):
#   return a / 2
# if is_even==int:
#   print(True)
# else:
#   print(False)

# print(is_even(2))

# # Find the Maximum
# # Write a function find_max(a, b) that takes two numbers and returns the larger one.

# a=int(input("enter random  #1 number : "))
# b=int(input("enter random  #2 number : "))

# def find_max(a,b) :
#   return a > b 

# if find_max == True :
#   print(a)
# else :
#   print(b)

# # Write a function reverse_string(text) that takes a string and returns it reversed.

# a=input("enter random word : ")

# def reverse_string(a) :
#   return  a[::-1]
# print(reverse_string(a))

# # Count Vowels in a String
# # Write a function count_vowels(text) that counts and returns the number of vowels (a, e, i, o, u) in a given string.

def count_vowels(text):
    vowels = "aeiou"
    counter = 0
    for i in text.lower():  
        if i in vowels:
            counter += 1
    return counter
print(count_vowels("maaam"))

# Check Divisibility
# Write a function is_divisible(a, b) that returns True if a is divisible by b, otherwise False. 

def divise(a, b):
    if a/b==True:
      print(True)
    else:
      print(False)

print(divise (8456,8456))