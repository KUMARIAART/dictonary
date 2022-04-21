"Write a Python program to combine values in python list of dictionaries. "
"Sample data: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]"
"Expected Output: Counter({'item1': 1150, 'item2': 300})"


my_dict=[{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
d = {}
for x in my_dict :
    if x['item'] not in d :
        d.update({x['item'] : x['amount']})
    else :
       d[x['item']] = d[x['item']] + x['amount']
print(d)

