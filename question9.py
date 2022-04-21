"Take input of name and marks of 10 students and store to a dictionary."

i=0
dic={}
while i<10:
    name=input("enter any name:-")
    marks=int(input("enter any marks:-"))
    dic.update({name:marks})
    i=i+1
print(dic)    

    