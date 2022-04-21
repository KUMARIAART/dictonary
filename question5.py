"Create a dictionary from 2 lists, where the elements of 1st list are the keys and the elements of the "
"2nd list are the corresponding values."

"Write a Python program to map two lists into a dictionary."

list1=["one","two","three","four","five"]
list2=[1,2,3,4,5,]
dic={} 
i=0
while(i<len(list1)):
    dic.update({list1[i]:list2[i]})
    i+=1
print(dic)


