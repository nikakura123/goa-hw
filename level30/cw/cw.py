#1)
def double_list_elements(num_list):
    list=[""]
    for i in num_list :
        list.append(i*2)
        return list
    print(double_list_elements[2,4,6,8])

#2)

def add_item(item_list,item): 
    item_list.append(item)
print(add_item([1,2,3,4],5))

#3)


def remove_item(list,item):
    list.remove(item)
    return list
print(remove_item([1,2,3,4],3))

#4)

def min_item(num_list):
    min_list=num_list[0]
    for i in num_list:
        if i < min_list :
            min_list = i
    return min_list
print(min_item([1024,360,202,4]))

