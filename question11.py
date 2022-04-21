"Count the total number of items from the values of the dictionary which are in the form of a list."
"Write a Python program to count the number of items in a dictionary value that is a list."

dict1 =  {
   'Alex': ['subj1', 'subj2', 'subj3'], 
   'David': ['subj1', 'subj2']}

sum=0
for i in dict1 :
    k=(len(dict1[i]))
    sum=sum+k
print(sum)    
    

    
     