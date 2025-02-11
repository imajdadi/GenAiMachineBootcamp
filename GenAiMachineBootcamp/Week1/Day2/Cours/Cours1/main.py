my_list = ['Rick', 'Sanchez']
print("My last name is:", my_list[1])
rick_dict = {
    'first_name':'Rick',
    'last_name':'Sanchez'
}
print("The last name of rick is:", rick_dict['last_name'])
a_dict = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}

print(a_dict.items())
# output : dict_items([('color', 'blue'), ('fruit', 'apple'), ('pet', 'dog')])

# The items() method returns a view object that displays 
# a list of dictionary's (key, value) tuple pairs.


#for key, value in a_dict.items():
    #print(key, '->', value)

# outputcolor -> bluefruit -> applepet -> dog 


sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"

}
keys_to_remove = ["name", "salary"]
print(sample_dict)