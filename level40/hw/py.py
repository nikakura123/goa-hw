

# 1) მომხმარებელს შემოატანინეთ მისი სახელი დიდი ასოებით და შეინახეთ ცვლადში სახელად name და .lower() ფუნქციის მეშვეობით გადააქციეთ ცვლადის მნიშვნელობა  პატარა ასოებად. 

# 2) ცვლადში შეინახეთ თქვენი გვარი პატარა ასოებით, შემდეგ .upper() ფუნქციის მეშვეობით გადააქციეთ ცვლადის მნიშვნელობა  დიდ ასოებად.

# 3) ცვლადში შეინახეთ სტრინგი პატარა ასოებით, შემდეგ .capitalize() ფუნქციის მეშვეობით გადააქციე პირველი ასო დიდ ასოდ.

# 4)ცვლადში შეინახეთ რაიმე სტრინგი,შემდეგ find() ფუნქციის მეშვეობით იპოვეთ რომელ ინდექსზეა კონკრეტული ასო

# 5)შექმენით სია სტრინგით და თითოეული სტრინგი გადაიყვანეთ დიდ ასოებად for ციკლის მეშვეობით


#1)
name = input("Enter your name: ").lower()
print(name)

#2)
surname = input("Enter your surname: ").upper()
print(surname)

#3)
string = input("Enter a string: ").capitalize()
print(string)

#4)
gnirts = "string"
print(gnirts.find("s"))

#5)
list = ["string", "list", "python"]
for i in list:
    print(i.upper())

