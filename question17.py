"Write a Python program to combine two dictionary adding values for common keys."
"d1 = {'a': 100, 'b': 200, 'c':300}"
"d2 = {'a': 300, 'b': 200, 'd':400}"
"Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})"

dic1 = {'a': 100, 'b': 200, 'c':300}
dic2 = {'a': 300, 'b': 200, 'd':400}
d={}
for x in dic1:
    for y in dic2:
        if x==y:
            num=dic1[x]+dic2[y]
            d[x]=num
        if x not in dic2:
            d[x]=dic1[x]
        if y not in dic1:    
            d[y]=dic2[y]
print(d)

