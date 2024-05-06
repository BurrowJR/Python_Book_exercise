names = ['Chris', 'Max', 'Karis', 'Victor']
upper_names = []
index = 0

while index < len(names):
    upper_name = names[index].upper()
    upper_names.append(upper_name)
    index += 1

print(upper_names)
print(names)

print()

names2 = ['Chris', 'Max', 'Karis', 'Victor']
upper_names2 = []

for name2 in names2:
    upper_name2 = name2.upper()
    upper_names2.append(upper_name2)

print(upper_names2)
print(names2)

print()

for char in 'Launch School'.split():
    print(char)

my_dict = {'a': 1, 'b': 2, 'c': 3}
for key in my_dict:
    print(key)
for value in my_dict.values():
    print(value)
for item in my_dict.items():
    print(item)
for key, value in my_dict.items():
    print(f'{key} = {value}')

print()

suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
ranks = [ '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

deck = []
for suit in suits:
    for rank in ranks:
        card = f'{rank} of {suit}'
        deck.append(card)

print(deck)

print()

numbers = [3, 1, 5, 9, 2, 6, 4, 7]
found_item = -1
index = 0

while index < len(numbers):
    if numbers[index] == 5:
        found_item = index
        break
    index += 1

print(found_item)

print()
forenames = ['Ken', 'Lynn', 'Pat', 'Nany']
surnames = ['Camp', 'Blake', 'Flanagan', 'Short']

index = 0
while index < len(forenames):
    if index >= len(surnames):
        break

    forename = forenames[index]
    surname = surnames[index]
    print(f'{forename} {surname}')

    index += 1

print()
print('using zip')
print()

zipped_names = zip(forenames, surnames)
for forename, surname in zipped_names:
    print(f'{forename} {surname}')

print()

squares = [ number * number for number in range(5)] # 0 * 0 for each # 0,1,2,3,4
          # 1*1 2*2 ... for the entire range
print(squares)

print()
# the for loop equivalent to the above code
squares = []
for number in range(5):
    square = number * number
    squares.append(square)

print(squares)

print()

multiples_of_6 = [ number for number in range(20) if number % 6 == 0 ]
print(multiples_of_6)

print()

even_squares = [ number * number for number in range(10) if number % 2 == 0 ]
# 1*1=1/2=.5 not printed
# 2*2=4/2=2  4 is printed
print(even_squares)

print()

cats_colors = {
    'Tess':     'brown',
    'Leo':      'orange',
    'Fluffy':   'gray',
    'Ben':      'black',
    'Kat':      'orange',     
}

names = [ name.upper() for name in cats_colors ]
print(names)
print()
names = [value for value in cats_colors.values()]
print(names)
print()
names = [(key, value) for (key, value) in cats_colors.items()]
print(names)
print()
names = [ name.upper() for name in cats_colors if cats_colors[name] == 'orange' ]
print(f' The orange colored cats names are {names}.')
print()
names = [ name.upper() for name in cats_colors if cats_colors[name] == 'orange' if name[0] == 'L' ]
print(names)

print()

suits = ['Culbs', 'Diamonds', 'Hearts', 'Spades']
rank = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

import pprint
deck = [ f'{rank} of {suit}'
        for suit in suits
        for rank in ranks ]
pprint.pp(deck)

print()

squares = { f'{number}-squared': number * number for number in range(1, 6) }
pprint.pp(squares)

print()
print('set and dict comprehensions are almost identical only sets do not use a :')
print()
squares = {number * number for number in range(1, 6)}
print(squares)

print()
# generator expression tuple
squares = (number * number for number in range(1, 6))
print(squares)


