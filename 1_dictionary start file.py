import random

phonebook = {}
phonebook = {'Chris':'555−1111',
             'Katie':'555−2222',
             'Joanne':'555−3333'}


'''
print()
print('*****  start section 1 - print dictionary ********')
print()

mydictionary = dict(m=9,n=9)
print(mydictionary)

print(len(phonebook))
print(type(phonebook))



print()
print('*****  end section 1 ********')
print()




print()
print('*****  start section 2 - search dictionary ********')
print()

name = "chris"
#phone = phonebook["Chris"]
#print(phone)

if name in phonebook:
    print()
else:
    print(f"{name} is not in the phonebook")

#what does the "f" mean????


print()
print('*****  end section 2 ********')
print()







print()
print('*****  start section 3 - edit/append dictionary ********')
print()

print(phonebook)

phonebook['Chris'] = '555-0123'
phonebook['Joe'] = '555-4444'

print(phonebook)
#since you cannot have a duplicated key, it will update Chris bc he already exists
#it appends Joe bc that key value does NOT exist


print()
print('*****  end section 3 ********')
print()






print()
print('*****  start section 4 - delete/remove from dictionary ********')
print()

print(phonebook)

del phonebook['Chris']

print(phonebook)
#shows you how to delete a key, if no key found, itll have an error and nothing is deleted

print()
print('*****  end section 4 ********')
print()


'''



print()
print('*****  start section 5 - iterate through keys, values, items ********')
print()

#how to iterate through a dictionary
for key in phonebook:
    print(f"the key is {key} and the value is {phonebook[key]}")

print()
for k in phonebook:
    print(f"the key is {k} and the value is {phonebook[k]}")
#what you use for your iterator is irrelavant as long as youre consistent
print()

for value in phonebook.values():
    print(value)
#the .value method is used to display the value SPECIFIC to dictionaries
print()

for k,v in phonebook.items():
    print(f"the key is {k} and the value is {v}")

print()
#if you DONT split the .item method up (only specifying ione variable) then it'll output a tuple, but if you split up 2 variables then itll output separate values you can manipulate
for ph_tuple in phonebook.items():
    print(ph_tuple)


print()
print('*****  end section 5 ********')
print()


'''

print()
print('*****  start section 6 - using get and clear ********')
print()

phone = phonebook.get("chris", "999")
print(phone)

phonebook.clear()
print(phonebook)



print()
print('*****  end section 6 ********')
print()



print()
print('*****  start section 7 - using pop method ********')
print()


remove = phonebook.pop("Chris", "not found")
print(remove)
print(phonebook)



print()
print('*****  end section 7 ********')
print()



print()
print('*****  start section 8 - using popitem ********')
print()

#pop item supposed to pick a random key value pair and remove the value
a = phonebook.popitem()

print(a)
print(phonebook)
#no randomness ALWAYS pops out the last value in the dictionary



print()
print('*****  end section 8 ********')
print()



print()
print('*****  start section 9 - using random and converting to list ********')
print()

phonebook_list = list(phonebook)
print(phonebook_list)

random_key = random.choice(phonebook_list)
print(random_key)
print(phonebook[random_key])
#random.choice only works on lists and displays a random key

#how to consolidate it onto 1 line of code:
print(phonebook[random.choice(list(phonebook))])


print()
print('*****  end section 9 ********')
print()


'''

