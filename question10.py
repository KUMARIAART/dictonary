"Store the unique letters and their frequency of the letters from the word MISSISSIPPI to a dictionarye"
"letters are the keys and their frequencies are the values."

"Write a Python program to create a dictionary from a string."
"Note: Track the count of the letters from the string."
"Sample string : 'w3resource'"
"Output: {'w': 1, '3': 1, 'r': 2, 'e': 2, 's': 1, 'o': 1, 'u': 1, 'c': 1}"

name=input("enter any name:-")
i=0
dic={}
while i<len(name):
    j=0
    count=0
    while j<len(name):
        if name[i]==name[j]:
            count=count+1
        j=j+1
    dic.update({name[i]:count})
    i=i+1
print(dic)            



    
    
    
    



