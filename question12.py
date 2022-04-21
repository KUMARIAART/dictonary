"Write a program to print the top 3 highest values of a given dictionary."
"Write a Python program to find the highest 3 values of corresponding keys in a dictionary."
my_dict = {
    'a':50,
    'b':58,
    'c':56,
    'd':40,
    'e':100,
    'f':20
}
max=0
second_max=0
third_max=0
j=[]
for i in my_dict:
    if my_dict[i]>max:
        max=my_dict[i] 
j.append(max)
for i in my_dict:
    if my_dict[i]>second_max:
        if my_dict[i]!=max:
            second_max=my_dict[i]
j.append(second_max)
for i in my_dict:
    if my_dict[i]>third_max:
        if my_dict[i]!=max:
            if my_dict[i]!=second_max:
                third_max=my_dict[i]
j.append(third_max)  
print(j)       


