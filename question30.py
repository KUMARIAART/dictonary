"Write a Python program to print all unique values in a dictionary. "

# "Sample Data : [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
"Expected Output : Unique Values: {'S005', 'S002', 'S007', 'S001', 'S009'}"

dic=[{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
x=[]
for i in dic:
    for j in i:
     if i[j] not in x:
        x.append(i[j])
print(x)  