"Write a Python program to get the maximum and minimum value in a dictionary."
dic= {
    'a':50, 
    'b':58,
    'c': 56,
    'd':40,
    'e':100, 
    'f':20
}
number=[]
for i in dic:
    number.append(dic[i])
print(number)
i=0
count=0
max_lenght=number[i]
while i<len(number):
    b=number[i]
    if b>max_lenght:
        max_lenght=b
    i+=1
print("maximum lenght list is:",max_lenght)
i=0
minimum_lenght=number[i] 
while i<len(number):
    b=number[i] 
    if b<minimum_lenght:
        minimum_lenght=b
    i+=1
print("minumum lenght list is :",minimum_lenght)           
