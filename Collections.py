seq = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(seq[3:7])
print(seq[-6: -2])
print(seq[2:8:2])
print(repr(seq[3:3]))
print(seq[:])
print(seq[::-1])

seq = [[1, 2], [3, 4]]
seq_dup = seq[:]
print(seq[0] is seq_dup[0])

print()
print('Exercises')
print('#1')
my_range = range(0, 25, 3)
print(list(my_range))
print(my_range[6])

print()
print('#2')
string = 'Launch School'
print(string[4:10])

print(string[4:4 + 6])

string = 'My cat is the best'
start = string.find('c')
print(string[start:start + 6])

print()
print('#3')
tuple1 = (1, 2, 3, 4, 5)
tuple2 = tuple1[3:0:-1]
print(tuple1)
print(tuple2)

my_tuple = (1, 2, 3, 4, 5)
my_list = list(my_tuple)
my_list.reverse()
result = tuple(my_list[1:4])
print(result)
result2 = my_tuple[-2:0:-1]
print(result2)
result3 = my_tuple[-2:-5:-1]
print(result3)

print()
print('#4')
pets = {
    'Cat':  'Meow',
    'Dog':  'Bark',
    'Bird': 'Tweet',
}
print(pets['Dog'])
print(pets.get('Lizard'))
print(pets.get('Lizard', '<silence>'))

print()
print('#5')
print('''
    Which of the following values can't be      
    used as a key in a dict object and why?
    "cat"
    (3, 1, 4, 1, 5, 9, 2)
    ["a", "b"]             # list; mutable
    {"a": 1, "b": 2}       # dict; mutable
    range(5)
    {1, 4, 9, 16, 25}      # set; mutable
    3
    0.0
    frozenset({1, 4, 9, 16, 25})
    # the rest are immutable built-in objects 
    and are acceptable dict keys.
    ''')

print()
print('#6')

print('abc-def'.isalpha())   # False
print('abc_def'.isalpha())   # False
print('abc def'.isalpha())   # False
print('abc def'.isalpha() and
       'abc def'.isspace())  # False
print('abc def'.isalpha() or 
      'abc def'.isspace())   # False
print('abcdef'.isalpha())    # True
print('31415'.isdigit())     # True
print('-31415'.isdigit())    # False
print('31_415'.isdigit())    # False
print('3.1415'.isdigit())    # False
print(''.isspace())          # False
print('  '.isspace())        # True
print('----'.isspace())      # False

print()
print('#7')
info = 'xyz:*:42:42:Lee Kim:/home/xyz:/bin/zsh'
print(info)
info2 = info.split(':')
print(info2)
info3 = '+'.join(info2)
print(info3)

result = info.replace(':', '+')
print(result)

print()
print('#8')
text = "It's probably pining for the fjords!"
print(text[21:35])
print(text[21:35].rfind('f'))
print(text)
print(text.rfind('f', 21, 35))

print()
print('#9')
stuff = [
    ['hello', 'world'],
    ['example', 'mem', None, 6, 88],
    [4, 8, 12],
]
stuff[1][3] = 606
print(stuff)

print()
print('#10')
cats = {
    'Pete': {
        'Cheddar': {
            'color': 'orange',
            'enjoys': {
                'sleeping',
                'snuggling',
                'meowing',
                'eating',
                'birdwatching',
            },
        },
        'Cocoa': {
            'color': 'black',
            'enjoys': {
                'eating',
                'sleeping',
                'playing',
                'chewing',
            },
        },
    }
}
print(cats['Pete']['Cocoa']['enjoys'])

print()
print('#11')
print('johnson' in 'Joe Johnson')     # False
print('sen' not in 'Joe Johnson')     # True
print('Joe J' in 'Joe Johnson')       # True
print(5 in range(5))                  # False
print(5 in range(6))                  # True
print(5 not in range(5, 10))          # False
print(0 in range(10, 0, -1))          # False
print(4 in {6, 5, 4, 3, 2, 1})        # True
print({1, 2, 3} in {1, 2, 3})         # False
print({3,2} in {1, frozenset({2,3})}) # True

print()
print('#12')
numbers1 = [1, 3, 5, 7, 9, 11]
numbers2 = []
numbers3 = [2, 4, 6, 8]
numbers4 = ['1', '3', '5']
numbers5 = ['1', 3.0, '5']
print(3 in numbers1)
print(3 in numbers2)
print(3 in numbers3)
print(3 in numbers4)
print(3 in numbers5)

print()
print('#13')
cats = ('Cocoa', 'Cheddar', 'Pudding', 'Butterscotch')
print('Butterscotch' in cats)  # True
print('Butter' in cats)        # False
print('Butter' in cats[3])     # True
print('cheddar' in cats)       # False

print()
print('#14')
my_str = 'abc'
my_list = ['Alpha', 'Bravo', 'Charlie']
my_tuple = (None, True, False)
my_range = range(10, 60, 10)

zipped_sequences = zip(my_str, my_list, my_tuple, my_range)
print(list(zipped_sequences))

print()
print('#15')
pets = {
    'Cat':  'Meow',
    'Dog':  'Bark',
    'Bird':  'Tweet',
}

print(pets)
print()
keys = pets.keys()
values = pets.values()
del pets['Dog']
pets['Snake'] = 'Sssss'
print(keys)
print()
print(values)
print()
print(pets)