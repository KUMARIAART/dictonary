"Write a Python program to print a dictionary in table format."
"my_dict = {'C1':[1,2,3],'C2':[5,6,7],'C3':[9,10,11]}"

"Sample Output:"
"C1 C2 C3"                                                                                                      
"1 5 9 "                                                                                                        
"2 6 10"                                                                                                        
"3 7 11"


my_dict = {'C1':[1,2,3],'C2':[5,6,7],'C3':[9,10,11]}
l=[]
for i in my_dict:
    print(i,end=" ")
    l.append(my_dict[i])
print()
i=0
while i<len(l):
    print(l[0][i],end='  ')
    print(l[1][i],end="  ")
    print(l[2][i],end="  ")
    print()
    i+=1




