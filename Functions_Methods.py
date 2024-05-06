)))
print(all(remainders_5(numbers_2)))
print(all(remainders_5(numbers_3)))
print(all(remainders_5(numbers_4)))
numbers = [2, 5, 8, 10, 13]
print([number % 2 == 0 for number in numbers])
# even numbers
print(any([number % 2 == 0 for number in numbers]))
print(all([number % 2 == 0 for number in numbers]))
print()

numbers = [5, 13]
print([number % 2 == 0 for number in numbers])
# even numbers
print(any([number % 2 == 0 for number in numbers]))
print(all([number % 2 == 0 for number in numbers]))
print()
numbers = [2, 8, 10,]
print([number % 2 == 0 for number in numbers])
# even numbers
print(any([number % 2 == 0 for number in numbers]))
print(all([number % 2 == 0 for number in numbers]))
print()
print('Exercises')
print('#1')
def set_foo():
    foo = 'bar'
    print(foo)  # This is in scope

set_foo()       # This is None
#print(foo) This is out of scope, will give an error
print()

print('#2')
foo = 'bar'       # This is outer scope

def set_foo():
    foo = 'qux'
    print(foo)    # This is inner scope

set_foo()         # This is None or empty
print(foo)        # This is outer scope
print()

print('#3')
first_number = input('Enter the first number: ')
second_number = input('Enter the second number: ')
number1 = float(first_number)
number2 = float(second_number)
product = number1 * number2
print(f'{number1} * {number2} = {product}')
print()

def multiply(left, right):
    return left * right

def get_number(prompt):
    entry = input(prompt)
    return float(entry)

first_number = get_number('Enter the first number: ')
second_number = get_number('Enter the second number: ')
product = multiply(first_number, second_number)

print(f'{first_number} * {second_number} = {product}')
print()

print('#4')
def multiply_numbers(num1, num2, num3):
    result = num1 * num2 * num3
    return result

product = multiply_numbers(2, 3, 4)
print(product)

#function name = multiply_numbers
#function arguments = (2, 3, 4)
#function definition = def and the following indentions lines 65,66,67
#function body = indentions lines 66, 67
#function parameters = def num1, num2, num3 line 65
#function invocation = multiply_numbers(2, 3, 4) line 69
#function return value = 24 the product line 69
#all identifiers = multiply_numbers, num1, num2, num3, result, and product
print()

print('#5')

def scream(words):
    return words + '!!!!'

scream('Yipeee')  #returns Yipeee but does not output anything to the screen without the print statement
print(scream('Yipeee'))
print()

print('#6')
def scream(words):
    words = words + '!!!!'
    return    # The return terminates 
              # the function
    print(words)

print(scream('Yipeee'))  # This now returns None
print('Nothing is printed the return terminates the function.')
print()

print('#7')
def foo(bar, qux):
    print(bar)
    print(qux)

#foo('Hello')  # This is missing an argument
foo('Hello', 'goodbye')
print()

print('#8')
def foo(bar, qux):
    print(bar)
    print(qux)

#foo(42, 3.141592, 2.718)
# This gives an error 2 arguments needed but 3 were given.
foo(42, 3.141592)
print()

print('#9')
def foo(first, second=3, third=2):
    # 3 and 2 are default values
    # you only have to give 1 argument
    print(first)
    print(second)
    print(third)

foo(42, 3141592, 2.718)
foo(42)
print()

print('#10')
def foo(first, second=3, third=2):
    print(first)
    print(second)
    print(third)

foo(42, 3.141592)
# only 1 argument has to be given the default numbers will be used 3 and 2
print()

print('#11')
def foo(first, second=3, third=2):
    print(first)
    print(second)
    print(third)

foo(42)
# output 42, 3, 2
print()

print('#12')
def foo(first=7, second=3, third=2):
    print(first)
    print(second)
    print(third)

foo()
# need at least 1 argument or first needs a default value
print()

print('#13')
#def foo(first, second=2, third):
def foo(first, second, third=2):
    print(first)
    print(second)
    print(third)

#foo(42)
foo(42, 10) #must have at least 2 arguments
# This gives us an error all subsequent parameters must have a default value
print()

print('#14')
# Identify all of the identifiers on each line
def multiply(left, right):   # multiply, left, right
    return left * right      # left, right

def get_num(prompt):         # get_num, prompt
    return float(input(prompt))  # float, input, prompt

first_number = get_num('Enter the first number: ')     # first_number, get_num
second_number = get_num('Enter the second number: ')     # second_number, get_num
product = multiply(first_number, second_number) # product, multiply, first_number, second_number
print(f'{first_number} * {second_number} = {product}')    # print, first_number, second_number, product
# def and return are key words
print()

print('#15')
def multiply(left, right):
    return left * right

def get_num(prompt):
    return float(input(prompt))

first_number = get_num('Enter the first number: ')
second_number = get_num('Enter the second number: ')
product = multiply(first_number, second_number)
print(f'{first_number} * {second_number} = {product}')

# Global
# multiply, get_num, first_number, second_number, product
# Local
# left, right, prompt
# Built_in
# float, input, print
print()

print('#16')
def multiply(left, right):
    return left * right

def get_num(prompt):
    return float(input(prompt))

first_number = get_num('Enter the first number: ')
second_number = get_num('Enter the second number: ')
product = multiply(first_number, second_number)
print(f'{first_number} * {second_number} = {product}')
# Function names:
# multiply; defined on line 211 and used on line 219, get_num; defined 214 and used on lines 217 and 218, float; built-in function used on line 215, input; built-in function used on line 215, print; built-in function used on line 220
# Parameters:
# left, right defined on line 211 and used on line 212, prompt definded on line 214 and used on line 215
print()

print('#17')
def say(message):
    print(f'--> {message}')

string1 = input()
string2 = input()

say(max(string1.upper(), string2.lower()))
# Function Names:  say
# Method Names:  upper and lower
# Built-in Function Names:  print, input, & max
print()

print('#18')
def remainders_3(numbers):
    return [number % 3 for number in numbers]

numbers_1 = [0, 1, 2, 3, 4, 5, 6]
numbers_2 = [1, 2, 4, 5]
numbers_3 = [0, 3, 6]
numbers_4 = []

print(any(remainders_3(numbers_1)))
print(any(remainders_3(numbers_2)))
print(any(remainders_3(numbers_3)))
print(any(remainders_3(numbers_4)))
print()

print('#19')
def remainders_5(numbers):
    return [number % 5 for number in numbers]

numbers_1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers_2 = [1, 2, 3, 4, 6, 7, 8, 9]
numbers_3 = [0, 5, 10]
numbers_4 = []

print(all(remainders_5(numbers_1