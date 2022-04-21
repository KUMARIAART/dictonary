"Write a Python script to add a key to a dictionary."

"Sample Dictionary : {0: 10, 1: 20}"
"Expected Result : {0: 10, 1: 20, 2: 30}"


dic={0: 10, 1: 20}
key=int(input("enter any key:-"))
Value=int(input("enter any value:-"))

dic.update({key:Value})
print(dic)


