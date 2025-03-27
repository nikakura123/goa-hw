# 1)კომენტარის მეშვეობით ახსენით .lower() / .upper() / .capitalize() / .find() ფუნქციების დანიშნულება

# 2)მომხმარებელს შემოატანინეთ მისი გვარი და შეამოწმეთ, თუ გვარის პირველი ასო არის დიდი ასო, მაშინ დაუბეჭდეთ "Hello", თუ არ არის მაშინ დაუბეჭდეთ "Bye"

# 3)მომხმარებელს შემოატანინეთ სახელი, შემდეგ შემოატანინეთ ასო და თუ ამ სახელში ეს ასო არიქნება, მაშინ გამოუტანეთ "Can't find character", 
# თუ იქნება მაშინ გამოუტანეთ "found it" და გვერდზე მიუწერეთ ამ ასოს ინდექსი

# 4)მომხმარებელს შემოატანინეთ მისი გვარი, შემდეგ შეეკითხეთ როგორ უნდა რო შეიცვალოს მისი გვარის ასოები, თუ გიპასუხებთ "upper" გადაიყვანეთ მთლიანი გვარი დიდ ასოებად, თუ გიპასუხებთ "lower" 
# გადაიყვანეთ მთლიანი გვარი პატარა ასოებად და თუ გიპასუხებთ "capitalize" 
# გადაიყვანეთ გვარის მხოლოდ პირველი ასო დიდ ასოდ.

#.1
#1) .lower() - აპატარავებს
#2) .upper() - ადიდებს
#3) .capitalize() - პირველ ასოს ადიდებს
#4) .find() - იპოვის სტრინგში სიმბოლოს ინდექსს

#.2
name = input("hi what's your name? : ")
sur_name = input("What's your surname? : ")

if sur_name[0].isupper():
    print("Hello", name,"!")
else:
    print("Bye", name)

#.3

name = input("What's your name? : ")
letter = input("Enter a letter: ")
if name.find(letter) == -1:
    print("Can't find character :(")
else:
    print("found it!",name.find(letter))

#.4
sur__name = input("What's your surname? : ")
answer = input("How do you want to change your surname? (upper/lower/capitalize) : ")

if answer == "upper":
    print(sur__name.upper())
elif answer == "lower":
    print(sur__name.lower())
elif answer == "capitalize":
    print(sur__name.capitalize())
else:
    print("invalid answer!")