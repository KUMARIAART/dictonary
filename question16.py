"Write a program such that the below given dictionaries are into a single dictionary and add the values"
"having same key."

dic1={1:10, 2:20}
dic2={3:30,2:40}
dic3={5:50,6:60}
d={}
for x in dic1:
    for y in dic2:
        if x==y:
            d.update({x:dic1[x]+dic2[y]})
        else:
            d.update({x:dic1[x]})
            d.update({y:dic2[y]})
dic={}
for i in dic3:
    for j in d:
        if i==j:
            dic.update({i:dic3[i]+d[j]})  
        else:
            dic.update({i:dic3[i]})  
            dic.update({j:d[j]}) 
print(dic)                      


