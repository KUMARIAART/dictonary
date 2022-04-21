"Take a list having dictionary elements as shown below (Sample Data) and then store all the unique "
"values into a list and print."


dic=[
    {"first":"1"}, 
    {"second": "2"},
    {"third": "1"},
    {"four": "5"},
    {"five":"5"},
    {"six":"9"},
    {"seven":"7"}
]
x=[]
for i in dic:
    for j in i:
     if i[j] not in x:
        x.append(i[j])
print(x)  
     
    