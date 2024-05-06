print('Composing function calls / Composition')
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def times(num1, num2):
    return num1 * num2

print(add(20, 45))
print(subtract(80, 10))
print(times(add(20, 45), subtract(80, 10)))

print()
total = add(20, 45)
difference = subtract(80, 10)
result = times(total, difference)
print(f'{result} = {total} * {difference}')
print()

print('Method Chaining')
tv_show = "Monty Python's Flying Circus"
#tv_show = tv_show.upper()
#tv_show = tv_show.split()
tv_show = tv_show.upper().split()
print(tv_show)
print()
letters = 'abcdefghijklmnopqrstuvwxyz'
consonants = (letters.replace('a', '').replace('e', '').replace('i', '').replace('o', '').replace('u', ''))
print(consonants)
print()
print('Modules is code you can make available to your program by importing it.')
print()
from datetime import datetime as dt
date = dt.strptime("August 19, 2014", "%B %d, %Y")
# %B tells strptime to look for the spelled-out month name
# %d tell strptime to look for the day of the month
# %Y tells strptime to look for the 4 digit year 
weekday_name = date.strftime('%A')
# to obtain the spelled-out weekday name(as given by %A)
print(weekday_name)

print()
def top():
    bottom()
def bottom():
    print('Reached the bottom')
top()

print()
greeting = 'Salutations'
def well_howdy(who):
    greeting = 'Howdy'
    print(f'{greeting}, {who}')
well_howdy('Angie')
print(greeting)

def well_howdy(who):
    global greeting
    greeting = 'Howdy'
    print(f'{greeting}, {who}')
well_howdy('Angie')
print(greeting)
print()

def outer():
    def inner1():
        def inner2():
            nonlocal foo
            foo = 3
            print(f"inner2 -> {foo} with id {id(foo)}")
        nonlocal foo
        foo = 2
        inner2()
        print(f"inner1 -> {foo} with id {id(foo)}")
    foo = 1
    inner1()
    print(f"outer -> {foo} with id {id(foo)}")
outer()
#print(f"global -> {foo} with id {id(foo)}")

print()
print('Exercises')
print('#1')
def do_something(dictionary):
    return sorted(dictionary.keys())[1].upper()

my_dict = {
    'Karl':     108,
    'Clare':    175,
    'Karis':    140,
    'Trevor':   180,
    'Antonina': 132,
    'Chris':    101,
}
print(do_something(my_dict))
print(sorted(my_dict))

print()
print('#2')
import math
print(math.sqrt(37))

from math import sqrt
print(sqrt(37))

import math as m
print(m.sqrt(37))

print()
print('#3')
def sum_of_square(num1, num2):
    def square(number):
        return number * number
    return square(num1) + square(num2)

print(sum_of_square(3, 4))
print(sum_of_square(5, 12))

print()
print('#4')
counter = 0
def increment_counter() :
    global counter
    counter += 1

print(counter)

increment_counter()
print(counter)

increment_counter()
print(counter)

counter = 100
increment_counter()
print(counter)

print()
print('#5')

def all_actions():
    counter = 0
    def increment_counter():
        nonlocal counter
        counter += 1
    print(counter)
    
    increment_counter()
    print(counter)

    increment_counter()
    print(counter)

    counter = 100
    increment_counter()
    print(counter)

all_actions()