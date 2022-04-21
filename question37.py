"Write a Python program to get the top three items in a shop. Go to the editor"
"Sample data: {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}"
"Expected Output:"
"item4 55"
"item1 45.5"
"item3 41.3"

my_dict={'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}

max=0
second_max=0
third_max=0
key1=0
key2=0
key3=0
for i in my_dict:
    if my_dict[i]>max:
        max=my_dict[i]
        key1=i
print(key1,max)
for i in my_dict:
    if my_dict[i]>second_max:
        if my_dict[i]!=max:
            second_max=my_dict[i]
            key2=i
print(key2,second_max)
for i in my_dict:
    if my_dict[i]>third_max:
        if my_dict[i]!=max:
            if my_dict[i]!=second_max:
                third_max=my_dict[i]
                key3=i
print(key3,third_max)       

    



