# ```
# 1.  ფუნქცია: ელემენტის მოძებნა
# შექმენი ფუნქცია find_item(item_list, item), რომელიც მიიღებს ორი პარამეტრი:
# item_list - სია ელემენტების.
# item - ელემენტი, რომლის შეძენა გსურს სიაში. ფუნქციამ უნდა დააბრუნოს True, თუ ელემენტი არსებობს სიაში და False, თუ არ არსებობს.

# 2. ფუნქცია: მაქსიმალური ელემენტი
# შექმენი ფუნქცია max_item(num_list), რომელიც მიიღებს რიცხვების სიას და დააბრუნებს ამ რიცხვებიდან ყველაზე დიდს.

# 3. დაასრულეთ საკლასო დავალება

# 4. ფუნქცია: ზრდა

# შექმენი ფუნქცია increment_list(num_list), რომელიც მიიღებს რიცხვების სიას და თითოეულ რიცხვს 1-ს მოუმატებს.

# 5. ფუნქცია: სიტყვის შებრუნება

# შექმენი ფუნქცია reverse_string(word), რომელიც მიიღებს სიტყვას და დააბრუნებს მას პირიქით.```


# #1)
# def find_item(item_list, item):
#     item_count = 0
#     for i in item_list:
#         if i == item:
#             item_count += 1
#     return item_count

# print(find_item(("nika"), "i"))

# #2)

# def find_max(item_list):

#     max_item = item_list[0]
#     for item in item_list:
#         if item > max_item:
#             max_item = item
#     return f"{max_item} is the most largest"
# item_list=[1,4,96,843,9971,628,38,8]
# print(find_max(item_list))

#3)

def increment_list(num_list):
    list=[""]
    for i in num_list :
        list.append(i+1)
        return list
    print(increment_list([2,4,6,8]))


#4)

def reverse_string(word):
  return word[::-1]

print(reverse_string("!dlroW ,eyb"))
