"To create a dictionary we put in the key value pairs in a comma separated form inside curly brackets "
"{ } and use the colon : to assign values to keys"

# city_population ={
#     "NewYorkCity":8550405,
#     "LosAngeles":3971883, 
#     "Toronto":2731571, 
#     "Chicago":2720546, 
#     "Houston":2296224, 
#     "Montreal":1704694, 
#     "Calgary":1239220, 
#     "Vancouver":631486, 
#     "Boston":667137
#     }

# print(city_population["NewYorkCity"])
# print(city_population)
# print(type(city_population))  
  
"You can create a dictionary using the dict() function."

# student=dict(name= "Ravina",age= 20)
# print(student)


# " nested dictionary :-"
# dic={
#     1: 'NAVGURUKUL',
#     2: 'IN', 
#     3:{
#          'A' : 'WELCOME',
#          'B' : 'To', 
#           'C' : 'DHARAMSALA'
#     }
# }
# print(dic)


"We can access dictionary values with the use of square brackets. Look at the example below to understand."

# person={
#     'name':'jack',
#     'age':20,
#     'gender':'male',
#     4:'organisation'}
# result = person['age'] 
# x = person.get("gender")
# print(person[4])
# print(x)
# print(result)


"We can also make use of the get() function to access dictionary values."

# person={
#     'name':'jack',
#     'age':20,
#     'gender':'male',
#     4:{
#         'organisation':'navgurukul','place':'dharamsala'
#     }
# }
# print(person['gender'])
# print(person[4])
# result = person[4]['place']
# print(result)


"In a python dictionary we can add only one key value pair at a time. To add to a dictionary we mention"
"the key inside square brackets [ ] and use the equal to = operator to assign a value."

# dic= {
#     'Name': 'RAM',
#      'Age': 17,
# }
# dic['ORGANIZATION'] = "NAV GURUKUL"
# dic['place'] = 'dharamsala'
# print(dic)


# dic= {
#     'Name': 'RAM',
#     'Age': 17,
# }
# dic['student']={
#     'id':22, 
#     'place':'dharamsala'
# }
# print(dic)

"We use the in keyword to check whether a given key exists or not in a dictionary."

# car ={
#     "brand":  "ford",
#     "model":  "mustang",
#     "year":  1964
# }
# if "model" in car:
#     print("Yes, 'model' is one of the keys in the car dictionary.")
# else:
#     print("No, 'model' key dictionary mai nahi hai.")

"To update dictionary ,we can make an entry in it or we can add a key-value pair or we can change the" 
"value of an existing key. As given in the example explained:-"

# person= {'1': 'RAM', '2': 17,}
# person[3] = 'male'
# print(person)

# details={
#     'Name': 'RAM',
#     'Age': 17, 
#     'student': {
#     'id': 22,
#     'place': 'dharamsala'
#     }
# }
# details['student']['id']=35
# print(details)


"We can copy a dictionary in two ways,first method is using copy() and second method by using built-in "
"function dict()."

# classes ={
#     "room1":  "6th",
#     "room2":  "7th",
#     "room3":  "8th"
# }
# mydict=classes.copy()
# print(mydict)


"Using the pop( ) method we can remove a specified element from the dictionary."

# CAR_DETAILS={
#     "brand": "Ford",
#     "model": "jason",
#     "year": 1964
# }
# CAR_DETAILS.pop("model")
# print(CAR_DETAILS)


"The popitem() method removes the last inserted item:"

# person={
#     'name':'jack',
#     'id':22,
#     'place':'dharamsala'
# }
# person.popitem()
# print(person)


# "Using the del keyword we can remove a specified element from the dictionary."

# person={
#     'name':'jack',
#     'id':22,
#     'place':'dharamsala'
# }
# del person('place')
# print(person)

"Iterate through all keys:-"

# states_capitals = {
#   'Gujarat' : 'Gandhinagar',
#   'Maharashtra' : 'Mumbai',
#   'Rajasthan' : 'Jaipur',
#   'Bihar' : 'Patna'
#   }
# for state in states_capitals:
#   print(state)


# "Iterate through all values:-"

# states_capitals = {
#     'Gujarat' : 'Gandhinagar',
#     'Maharashtra' : 'Mumbai',
#     'Rajasthan' : 'Jaipur',
#     'Bihar' : 'Patna'
# }
# for state in states_capitals:
#     print(states_capitals[state])


# details ={
#     "name":  "Bijender",
#     "age":  17,
#     "class":  "10th"
# }
# for x in details.values():
#     print(x)

"How to print keys and values together from a dictionary?"

# movie ={
#     "name":  "Puli",
#     "hero":  "Vijay",
#     "rating":  7.5
# }
# for x,y in movie.items():
#     print(x,y)


"We use Dictionary length to find the number of items/key value pairs in a dictionary."

# meal ={
#     "monday":  "Chole chawal",
#     "sunday":  "Fried rice",
#     "wednesday":  "dosa"
# }
# print(len(meal))

















   






