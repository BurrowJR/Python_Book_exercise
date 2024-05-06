print('Exercises')
print('#1')
my_object1 = ['Hello']
my_object2 = ['Hello']
my_object3 = my_object1
#Does NOT apply to immutable objects like; strings and tuples
print(my_object1 == my_object2)  #True
print(my_object1 is my_object2)  #False
print(my_object3 == my_object1)  #True
print(my_object3 is my_object1)  #True
print(my_object2 == my_object3)  #True
print(my_object2 is my_object3)  #False
print()
a = 'hat'
b = 'hat'
c = a
print(a == b)  #True
print(a is b)  #True
print(b == c)  #True
print(b is c)  #True
print(a == c)  #True
print(a is c)  #True
print('== compares two objects to see whether they are equal. They are considered equal when they have the same value or state.  In the case of collections, two collections are equal when they have the same elements.')
print()
print('is checks two variables to see whether they reference the same object.  An object is the same as another object if both are stored at the same location in memory.  In particular, that means we can say that they share the referenced object or that they are aliases for the same object.')

print()
print('#2')
set1 = {42, 'Monty Python', ('a', 'b', 'c')}
set2 = set1  #points to the same place in memory
set1.add(range(5, 10))
print(set1)
print()
print(set2)
print(set1 == set2)
print(set1 is set2)
#they are stored at the same place in memory 
#assigning a variable to another variable doesn't create a new object, but copies a reference from the original variable

print()
print('#3')
dict1 = {
    "Hitchhiker's Guide to the Galaxy":  42,
    "Monty Python":  "The Life of Brian",
    "Airplane!":  "Don't call me Shirley!",
}
dict2 = dict(dict1)  # creates a new dict
dict2["Monty Python"] = "Holy Grail"
#changes only dict2; dict1 stays the same
print(dict1["Monty Python"])
print(dict1 == dict2)
print(dict1 is dict2)
print()
print(dict1)
print()
print(dict2)

print()
print('#4')
dict1 = {
    'a':  [1, 2, 3],
    'b':  (4, 5, 6),  #tuple can not change
}
dict2 = dict(dict1) #create a new shallow copy
dict1['a'][1] = 42  # shares the same list
print(dict2['a'])   # so both dict will change
print(dict1)
print(dict2)
print()
print(dict1 == dict2) #only shares the list
print(dict1 is dict2) #not the same space in memory

print()
print('#5')
import copy
dict1 = {
    'a':  [[7, 1], ['aa', 'aaa']],
    'b':  ([3, 2], ['bb', 'bbb']),
}
dict2 = copy.deepcopy(dict1)
#creates entirely new objects, including their nested contents. however strings and tuples are immutuble
print(dict1         is dict2)
print(dict1['a']    is dict2['a'])
print(dict1['a'][0] is dict2['a'][0])
print(dict1['a'][1] is dict2['a'][1])
print(dict1['b']    is dict2['b'])
print(dict1['b'][0] is dict2['b'][0])
print(dict1['b'][1] is dict2['b'][1])
print()
print(dict1['a'][0][0] is dict2['a'][0][0])
print(dict1['a'][0][1] is dict2['a'][0][1])
print(dict1['a'][1][0] is dict2['a'][1][0])
print(dict1['a'][1][1] is dict2['a'][1][1])
print(dict1['b'][0][0] is dict2['b'][0][0])
print(dict1['b'][0][1] is dict2['b'][0][1])
print(dict1['b'][1][0] is dict2['b'][1][0])
print(dict1['b'][1][1] is dict2['b'][1][1])

print()
print('#6')
dict1 = {
    'a':  [[7, 1], ['aa', 'aaa']],
    'b':  ([3, 2], ['bb', 'bbb']),
}
dict2 = dict(dict1)
#shallow copy they are different objects, but the nested components are all references to the original nested objects
print(dict1         is dict2)
print(dict1['a']    is dict2['a'])
print(dict1['a'][0] is dict2['a'][0])
print(dict1['a'][1] is dict2['a'][1])
print(dict1['b']    is dict2['b'])
print(dict1['b'][0] is dict2['b'][0])
print(dict1['b'][1] is dict2['b'][1])
print()
print(dict1['a'][0][0] is dict2['a'][0][0])
print(dict1['a'][0][1] is dict2['a'][0][1])
print(dict1['a'][1][0] is dict2['a'][1][0])
print(dict1['a'][1][1] is dict2['a'][1][1])
print(dict1['b'][0][0] is dict2['b'][0][0])
print(dict1['b'][0][1] is dict2['b'][0][1])
print(dict1['b'][1][0] is dict2['b'][1][0])
print(dict1['b'][1][1] is dict2['b'][1][1])
