my_str = 'Python'
print(my_str)

my_list = list(my_str)  # [ ]  list
print(my_list)

my_tuple = tuple(my_list)  # ( ) tuple
print(my_tuple)

my_set = set(my_tuple)  # { }  set
print(my_set)

print()

print('Exercises')
print('#1')

people = ['dog', 'cat', 'bird', 'fish']
print(len(people))
people = 'people'
print(len(people))

print()
print('#2')
stuff = ('hello', 'world', 'bye', 'now')
print(stuff)
stuff_list = list(stuff)
stuff_list[2] = 'goodbye'
print(stuff_list)
stuff = tuple(stuff_list)
print(stuff)

print()
print('#3')
print('2 differences between lists and tuples: list are mutable, tuples are not; list use [], tuples use ()')
print('2 similarities: They both use sequences as ordered collections for numeric indexes; they are heterogeneous, elements do not have to be the same type.')

print()
print('#4')
print('Why can we treat strings as sequences?')
print('Strings are ordered; you can access the individual characters within indexing.')

print()
print('#5')
print('How do the set types differ from the sequence types? :  Sets are unordered; they do not support indexing. Tuples, strings, and list maintain their order, they are sequence types. Sets do not allow duplicate values.')

print()
print('#6')
pi = 3.141592
str_pi = str(pi)
print(type(str_pi))

print()
print('#7')
def print_range(my_range):
    print(list(my_range))

print_range(range(7))
print_range(range(1, 6))
print_range(range(3, 15, 4))
print_range(range(3, 8, -1))
print_range(range(8, 3, -1))

print()
print('#8')
print(list(range(3, 17, 4)))

print()
print('#9')
my_list = [1, 2, 3, [4, 5, 6]]
another_list = list(my_list)
print(my_list == another_list)
# true yes contain the same values
print(my_list is another_list)
# False they have a different place in memory they are not the same object in memory
print(my_list[3] == another_list[3])
#true they contain the same elements and value
print(my_list[3] is another_list[3])
# true the nested copies point to the same location in memory this is a shallow copy

print()
print('#10')
names = {'Chris', 'Clare', 'Karis', 'Karl', 'Max', 'Nick', 'Victor' }
print(names) # sets are unordered collections 

print()
print('#11')
country = {
    'Alice':      'USA',
    'Francois':   'Canads',
    'Inti':       'Peru',
    'Monika':     'Germany',
    'Sanyu':      'Uganda',
    'Yoshitaka':  'Japan',
}
print(country['Sanyu'])
print(country['Alice'])