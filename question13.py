"Write a program to create a dictionary with all numbers from 1 to 15 as the keys and their squares as "
"the corresponding values."

"Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in"
"the form (x, x*x)."
"Sample input ( n = 5) :"
"Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}."

"Q4. Write a Python script to print a dictionary where the keys are numbers    between 1 and 15 "
"(both included) and the values are square of keys."
"Simple Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144"
"69, 14: 196, 15: 225}."

"Q10.Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included)" 
"and the values are square of keys. Sample Dictionary"
"{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}"

n=int(input("enter any number:-"))
i=1
dic={}
while i<=n:
    dic.update({i:i*i})
    i=i+1
print(dic)    
