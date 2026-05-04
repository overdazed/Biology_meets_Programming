# Write a for-loop that iterates over start_list 
# and .append()s each number squared (x ** 2) to square_list.

# Then sort square_list!

start_list = [5, 3, 1, 2, 4]
square_list = []

# Your code here!
for number in start_list:
  square_list.append(number ** 2)
  square_list.sort()

print (square_list)


# A dictionary is similar to a list, but you access 
# values by looking up a key instead of an index. 
# A key can be any string or number. 
# Preview: Docs Loading link description
# Dictionaries
#  are enclosed in curly braces, like so:

d = {'key1' : 1, 'key2' : 2, 'key3' : 3}

# This is a dictionary called d with three key-value pairs. 
# The key 'key1' points to the value 1, 'key2' to 2, and so on.

# Dictionaries are great for things like phone books (pairing a name with a phone number), 
# login pages (pairing an e-mail address with a username), and more!

# Print the values stored under the 'Sloth' and 'Burmese Python' keys. 
# Accessing dictionary values by key is just like accessing list values by index:

# Assigning a dictionary with three key-value pairs to residents:
residents = {'Puffin' : 104, 'Sloth' : 105, 'Burmese Python' : 106}

print residents['Puffin'] # Prints Puffin's room number

# Your code here!
print residents['Sloth']
print residents['Burmese Python']

# Like Lists, Dictionaries are mutable. 
# This means they can be changed after they are created. 
# One advantage of this is that we can add new key/value pairs 
# to the dictionary after it is created like so:

dict_name[new_key] = new_value


# An empty pair of curly braces {} is an empty dictionary, 
# just like an empty pair of [] is an empty list.

# The length len() of a dictionary is the number of key-value pairs it has. 
# Each pair counts only once, even if the value is a list. 
# (That’s right: you can put lists inside dictionaries!)

# Add at least three more key-value pairs to the menu variable, 
# with the dish name (as a "string") for the key and 
# the price (a float or integer) as the value. Here’s an example:
menu = {} # Empty dictionary
menu['Chicken Alfredo'] = 14.50 # Adding new key-value pair
print menu['Chicken Alfredo']

# Your code here: Add some dish-price pairs to menu!
menu['Spam'] = 2.50
menu['Eggs'] = 1.50
menu['Water'] = 1.50

print "There are " + str(len(menu)) + " items on the menu."
print menu

# Because dictionaries are mutable, they can be changed in many ways. 
# Items can be removed from a dictionary with the del command:

del dict_name[key_name]

# will remove the key key_name and its associated value from the dictionary.

# A new value can be associated with a key by assigning a value to the key, like so:

dict_name[key] = new_value

# Delete the 'Sloth' and 'Bengal Tiger' items from zoo_animals using del.

# Set the value associated with 'Rockhopper Penguin' to anything other than 'Arctic Exhibit'.

# key - animal_name : value - location 
zoo_animals = { 'Unicorn' : 'Cotton Candy House',
'Sloth' : 'Rainforest Exhibit',
'Bengal Tiger' : 'Jungle House',
'Atlantic Puffin' : 'Arctic Exhibit',
'Rockhopper Penguin' : 'Arctic Exhibit'}
# A dictionary (or list) declaration may break across multiple lines

# Removing the 'Unicorn' entry. (Unicorns are incredibly expensive.)
del zoo_animals['Unicorn']

# Your code here!
del zoo_animals['Sloth']
del zoo_animals['Bengal Tiger']
zoo_animals['Rockhopper Penguin'] = 'Anything other'

print zoo_animals


# Sometimes you need to remove something from a list.

beatles = ["john","paul","george","ringo","stuart"]
beatles.remove("stuart")
print beatles

# This code will print:
["john","paul","george","ringo"]

# 1. We create a list called beatles with 5 strings
# 2. Then, we remove the first item from beatles that matches the string "stuart". 
# Note that .remove(item) does not return anything.
# 3. Finally, we print out that list just to see that "stuart" was actually removed.

# Remove 'dagger' from the list of items stored in the backpack variable.
backpack = ['xylophone', 'dagger', 'tent', 'bread loaf']
backpack.remove("dagger")


Let’s go over a few last notes about dictionaries

my_dict = {
  "fish": ["c", "a", "r", "p"],
  "cash": -4483,
  "luck": "good"
}
print my_dict["fish"][0]


# Let’s go over a few last notes about dictionaries

my_dict = {
  "fish": ["c", "a", "r", "p"],
  "cash": -4483,
  "luck": "good"
}
print my_dict["fish"][0]


# 1. In the example above, we created a dictionary that holds many types of values.
# 2. The key "fish" has a list, the key "cash" has an int, and the key "luck" has a string.
# 3. Finally, we print the letter "c". When we access a value in the dictionary like my_dict["fish"], 
# we have direct access to that value (which happens to be a list). 
# we can access the item at index 0 in the list stored by the key "fish".

# 1. Add a key to inventory called 'pocket'

# Set the value of 'pocket' to be a list consisting of the strings 'seashell', 
# 'strange berry', and 'lint'

# .sort() the items in the list stored under the 'backpack' key

# Then .remove('dagger') from the list of items stored under the 'backpack' key

# Add 50 to the number stored under the 'gold' key

inventory = {
  'gold' : 500,
  'pouch' : ['flint', 'twine', 'gemstone'], # Assigned a new list to 'pouch' key
  'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
}

# Adding a key 'burlap bag' and assigning a list to it
inventory['burlap bag'] = ['apple', 'small ruby', 'three-toed sloth']

# Sorting the list found under the key 'pouch'
inventory['pouch'].sort() 

# Your code here
inventory['pocket'] = ['seashell', 'strange berry', 'lint']
inventory['backpack'].sort()
inventory['backpack'].remove('dagger')
inventory['gold'] += 50