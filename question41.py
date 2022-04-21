"Q38.. Write a Python program to drop empty Items from a given Dictionary. "
"Original Dictionary:{'c1': 'Red', 'c2': 'Green', 'c3': None}"
"New Dictionary after dropping empty items:{'c1': 'Red', 'c2': 'Green'}"



dict1={'c1': 'Red', 'c2': 'Green', 'c3': None}
j={}
for i in dict1:
    if dict1[i]==None:
        pass
    else:
        j.update({i:dict1[i]})
print(j)


