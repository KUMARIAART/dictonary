"Write a Python script to merge two Python dictionaries"

dic1={'umesh':21,'bijender':54,'amar':67,'peter':89,'sonu':56}
dic2={'python':20,"gaurav":300,'dev':34,"karan":43}
dic={}
for i in (dic1,dic2):
    dic.update(i)
print(dic)

