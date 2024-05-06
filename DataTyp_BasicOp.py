# Data Types and Basic Operations

#Infinite Loop
#import time
#while True:
  #time.sleep(1)
  #print(time.#asctime())
print()
print('Data Type Exercise')
print('#1')
print(type('True'))        #str
print(type(False))         #bool
print(type((1, 2, 3)))     #tuple
print(type(1.5))           #flost
print(type([1, 2, 3]))     #list
print(type(2))             #int
print(type(range(5)))      #range
print(type({1, 2, 3}))     #set
print(type(None))          #NoneType
print(type({'foo': 'bar'}))#dict
print()
print('#2')
print('Create a tuple called names')
names = (
    'Asta', 
    'Butterscotch', 
    'Pudding', 
    'Neptune', 
    'Darwin',               # add a trailing comma
)                           # line up with beginning
print(names)
print()
print('#3')
print('Create a dictionary named pets')
pets = {
    'Asta':               'dog',
    'Butterscotch':       'cat',
    'Pudding':            'cat',
    'Neptune':            'fish',
    'Darwin':             'lizard',
}

print(pets)

print(0.1 + 0.2 == 0.3)

import math
print(math.isclose(0.1 + 0.2, 0.3))

from decimal import Decimal
print(Decimal('0.1') + Decimal('0.2') == Decimal('0.3'))
print('5' < 'A') #True
print('a' < 'A') #False

print({3, 2, 4} < {1, 2, 3})   #False
print({3, 2, 4} == {1, 2, 3})  #False
print({1, 2, 3} < {3, 2, 4})   #False
print({1, 2, 3} == {1, 2, 3})  #True

print('foo' + 'bar')
print('1' + '2')
print('foobar' * 3)
print(3 * 'foobar')
print(int('5')+ int('5')) #10
print('5' + '5')          #55
print(str(5) + str(5))    #55

print(3)
print(str('hello'))   # Explicit coercion
print('hello')       #inplicit coercion
print(True + True + True)   # 3
print(False * 3)   # 0

print(type(1))
print(type(True))
print(type(None))
print(type('abc').__name__)
print(type([]).__name__)
print(type('abc') is str)
print(type(False) is bool)
print()
print(isinstance('abc', str))
print(isinstance([], set))
print('line 67')
class A:
  pass
class B(A):
  pass
print(A)
print(B)
print()
b = B()
print(b)
print()
print(type(b).__name__)  # B
print(type(b) is B)      # True
print(type(b) is A)      # False (b's type is not A)
print(isinstance(b, B))  # True
print(isinstance(b, A))  # True (b is instance of A and B)
print()
print(list(range(5, 15)))
print(list(range(5, 15, 2)))
print(len(range(5, 15, 2)))
print()
print(4 * 5 - 1 + 2 * 3)
print((4 * (( 5 - 1) + 2)) * 3)
print(((((4 * 5) -1) + 2) * 3))
print(4 * (5 - ( 1 + ( 2 * 3))))
# Always use parentheses to explicitily evarlate the expression
print()
print('Basic Operations Exercises')
print('#1')
print('Johnna' + ' ' + 'Burrow')

first_name = 'Johnna'
last_name = 'Burrow'

print(f'Hello, my name is {first_name} {last_name}.')
print()
print('#2')
num = 4936
ones = (num % 10)
print(f'Ones place is {ones}.')
tens = int(num % 100 / 10) 
print(f'Tens place is {tens}.')
hund = int(num % 1000 / 100)
print(f'Hundreds place is {hund}.')
thous = int(num / 1000)
print(f'Thousands place is {thous}.')
# can use // instead of int
ten = (num % 100 // 10)
print(f'{ten} is in the tens place using // instead of int.')
print()
print('#3')
print('What does the following code do? Why?')
print()
print("The following code prints out 510 because '5' and '10' are strings so the print command concatenates them.")
print('5' + '10')
print()
print('#4')
print('Refactor the code form the previous exercise to use coercion to print 15 instead.')
print(int('5') + int('10'))
print()
print('#5')
print(
  "Will an error occur if you try to access a list element with an index greater than or equal to the list's length?"
  )
print(
  "The answer is yes, it will give you a 'list index out of range' error. You can not list an index with no corresponding element.")
foo = ['a', 'b', 'c']
#print(foo[3])  will give an error
print(foo[2])
print()
print('#6')
print('To what value does the following expression evaluate?  "foo" == "Foo" ')
print('foo' == 'Foo')   # this is False capitalization matters
print('foO'.casefold() == 'Foo'.casefold())  # casefold will lower case the string
print()
print('#7')
print("What will the following code do? Why? int('3.1415')")
print("This will give you an 'invalid literal for int() with base 10: '3.1415'. This is a string so to change it to an integer you must first make it a float then an integer.")
#print(int('3.1415'))
num = float('3.1415')
num = int(num)
print(num)
print()
print('#8')
print("To what value does the following expression evaluate?   '12' < '9' ")
print('This is True because it is a string 1 is less than 9 if it was an integer then it would be False.')
print('12' < '9')
print(12 < 9)
