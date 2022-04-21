"Write a program remove the first key value pair from a nested dictionary."

Dic= {
    1: 'NAVGURUKUL',
    2: 'IN',
     3:{
         'A' : 'WELCOME',
         'B' : 'To',
         'C' : 'DHARAMSALA'
     }
}
for i in Dic.values():
    if type(i)==dict:
        for j in i:
            del i[j]
            break
print(Dic)        

