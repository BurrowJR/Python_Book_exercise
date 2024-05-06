print('#1')
counter = 0
while counter < 5:
    print(counter)
    counter += 1 # wihout this the loop condition is always Truthy so it never stops you must increment counter or it stays at 0

print()

print('#2')
#age = int(input('How old are you?  '))
age = 20
print()
print(f'You are {age} years old.')

for future in range(10, 50, 10):
    print(f'In {future} years, you will be {age + future} years old.')

print()

print('#3')

my_list = [6, 3, 0, 11, 20, 4, 17]
index = 0
while index < len(my_list):
    number = my_list[index]
    print(number)
    index += 1
print()
for number in my_list:
    print(number)

print()

print('#4')
print('Even numbers')
my_list = [6, 3, 0, 11, 20, 4, 17]
index = 0
while index < len(my_list):
    number =my_list[index]
    if number % 2 == 0:
        print(number)
    index += 1

print()
print('Odd numbers')
for number in my_list:
    if number % 2 != 0:
        print(number)

print()

print('#5')
my_list = [
    [1, 3, 6, 11],
    [4, 2, 4],
    [9, 17, 16, 0],
]
for nested_list in my_list:
    for number in nested_list:
        if number % 2 == 0:
            print(number)

print()

print('#6')
my_list = [1, 3, 6, 11, 4, 2, 4, 9, 17, 16, 0]
new_list = []
for number in my_list:
    if number % 2 == 0:
        new_list.append('even')
    if number % 2 != 0:
    #else:
        new_list.append('odd')

print(new_list)
print()
# could also have used ternary expression in the comprehension
result = ['even' if number % 2 == 0 else 'odd' for number in my_list]
print(result)
print()
#use a helper function to determine whether we should add 'even' or 'odd'
def odd_or_even(number):
    return 'even' if number % 2 == 0 else 'odd'
result = [odd_or_even(number)for number in my_list]
print(result)

print()
    
print('#7') 
def find_integers(things):
    return [element for element in things if type(element) is int]
print()
def find_integers(things):
    result = []
    for element in things:
        if type(element) is int:
            result.append(element)
    return result

my_tuple = (1, 'a', '1', 3, [7], 3.1415, -4, None, {1, 2, 3}, False)

integers = find_integers(my_tuple)
print(integers)

print()

print('#8')
my_set = {
    'Fluffy',
    'Butterscotch',
    'Pudding',
    'Cheddar',
    'Cocoa',
}
my_dict = {name: len(name) 
           for name in my_set
           if len(name) % 2 != 0 }
print(my_dict)
print()
my_dict = {name: len(name) for name in my_set}
print(my_dict)

print()
print('#9')
def factorial(n):
    result = 1
    for number in range(n, 0, -1):
        result *= number
    return result

print(factorial(5))
print(factorial(8))

def factorial(n):
    result = 1
    while n > 0:
        result *= n
        n -= 1
    return result

print(factorial(4))
print(factorial(3))

print()
print('#10')
import random

highest = 10
number = random.randrange(highest + 1)
print(number)
print()
while number != highest:
    number = random.randrange(highest + 1)
    print(number)

print('Refactor the code so it does not require two different invocations of randrange.')
print()
import random

highest = 10
while True:
    number = random.randrange(highest + 1)
    print(number)
    if number == highest:
        break

print()
print('#11')
my_list = [
    [1, 3, 6, 11],
    [4, 2, 4],
    [9, 17, 16, 0],
]
outer_index = 0
while outer_index < len(my_list):
    nested_list = my_list[outer_index]
    print(nested_list)
    inner_index = 0
    while inner_index < len(nested_list):
        number = nested_list[inner_index]
        print(number)
        
        inner_index += 1

    outer_index += 1
print('even numbers of my_list')
outer_index = 0
while outer_index < len(my_list):
    nested_list = my_list[outer_index]
    inner_index = 0
    while inner_index < len(nested_list):
        number = nested_list[inner_index]
        if number % 2 == 0:
            print(number)
        inner_index += 1
    outer_index += 1