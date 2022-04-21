"Write a Python program to multiply all the items in a dictionary."

dict1={3: 4, 4: 3, 1: 2, 2: 1, 7:4}
sum=1
for i in dict1:
    sum=sum*i*dict1[i]
print(sum)


sum=1
for i in dict1.values():
    sum=sum*i
print(sum)    


sum=1
for i in dict1.keys():
    sum=sum*i
print(sum)  
  
sum=1
for i in dict1:
    sum=sum*dict1[i]
print(sum)

