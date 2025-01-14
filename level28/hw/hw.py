
def add_numbers(a, b):
  return a + b

print(add_numbers(2,4))


# Check Even or Odd
# Write a function is_even(number) that returns True if a number is even, otherwise False.

def is_even(number):
  if number % 2 == 0:
    return "Even"
  else:
    return "False"
  
print(is_even(16))

# Find the Maximum
# Write a function find_max(a, b) that takes two numbers and returns the larger one.

def find_max(a, b):
  if a > b:
    return f"{a} is larger"
  else:
    return f"{b} is larger"
  
print(find_max(2,4))


# Write a function reverse_string(text) that takes a string and returns it reversed.

def reverse_string(text):
  return text[::-1]

print(reverse_string("Hello, World!"))

# Count Vowels in a String
# Write a function count_vowels(text) that counts and returns the number of vowels (a, e, i, o, u) in a given string.

def count_vowels(text):
  vowels = "aeiou"
  count = 0
  for i in text:
    if i in vowels:
      count += 1
  return count

print(count_vowels("dachi"))

# Check Divisibility
# Write a function is_divisible(a, b) that returns True if a is divisible by b, otherwise False.

def is_divisible(a, b):
  if b == 0:
    return False
  else:
    return True
  
print(is_divisible(2, 0))