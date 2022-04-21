"Write a Python program to sum all the items in a dictionary."

dict1={1:2,2:3,3:4,4:5}
sum=0
for i in dict1:
    sum=sum+i+dict1[i]
print(sum)
