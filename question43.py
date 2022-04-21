"Q40. Write a Python program to convert more than one list to nested dictionary. "
"Original strings:"
"['S001', 'S002', 'S003', 'S004']"
"['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']"
"[85, 98, 89, 92]"
"Nested dictionary:"
"[{'S001': {'Adina Park': 85}}, {'S002': {'Leyton Marsh': 98}}, {'S003': {'Duncan Boyle': 89}}, {'S004': {'Saim Richards': 92}}]"


# n=int(input("enter any number:-"))
# if n %2!=0:
#     print("weird")
# elif n>=2 and n<=5:
#     print("not weird") 
# elif n>=6 and n<=20:
#     print("weird")  
# else:
#     print("not weird")     

# if n%2 != 0:
#     print("Weird")
# else:
#     if n>=2 and n<5:
#         print("Not Weird") 
#     elif n>=6 and n<=20:
#         print("Weird")  
#     elif n>20:
#         print("Not Weird")     

# n=int(input())
# i=0
# while i<n:
#     print(i**2)
#     i+=1

# def is_leap(year):
#     if year%100==0:
#         if year%400==0:
#             return(True)
#         else:
#             return(False) 
#     elif year%4==0:
#         return(True)
#     else:
#         return(False)    
# year = int(input())
# print(is_leap(year))

# n = int(input())
# i=1
# while i<=n:
#     print(i,end="")
#     i+=1

# def print_full_name(first,last):
#     last= last+"!"
#     print("Hello",first, last,"You just delved into python.")
# if __name__ == '__main__':
#     first_name = input()
#     last_name = input()
#     print_full_name(first_name, last_name)

# n = int(input())
# arr = map(int, input().split())
# print(sorted(list(set(arr)))[-2])

# n = int(input())
# student_marks = {}
# for _ in range(n):
#     name, *line = input().split()
#     scores = list(map(float, line))
#     student_marks[name] = scores
# query_name = input()
# marks=0
# for i in student_marks[query_name]:
#     marks=marks+i
#     avg=marks/3
#     print("%.2f"%avg)


    

    