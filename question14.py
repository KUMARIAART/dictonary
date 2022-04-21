"Write a program to print the top 3 highest values of a given dictionary."

my_dict = {
    'a':50, 
    'b':58,
    'c': 56,
    'd':40,
    'e':100, 
    'f':20
}

max=0
second_max=0
third_max=0
key1=0
key2=0
key3=0
j=[]
for i in my_dict:
    if my_dict[i]>max:
        max=my_dict[i]
        key1=i
j.append(key1)
for i in my_dict:
    if my_dict[i]>second_max:
        if my_dict[i]!=max:
            second_max=my_dict[i]
            key2=i
j.append(key2)
for i in my_dict:
    if my_dict[i]>third_max:
        if my_dict[i]!=max:
            if my_dict[i]!=second_max:
                third_max=my_dict[i]
                key3=i
j.append(key3)  
print(j)       

