#value = int(input('Enter a number: '))
from asyncio.constants import SENDFILE_FALLBACK_READBUFFER_SIZE


value = 3
if value == 3:
    print('value is 3')
elif value == 4:
    print('value is 4')
else:
    print('value is NOT 3 or 4')

print()

value = 5             # 5 is truthy
if value:
    print(f'{value} is truthy')
else:
    print(f'{value} is falsy')

value = 0              # 0 is falsy
if value:
    print(f'{value} is truthy')
else:
    print(f'{value} is falsy')

print()

print(3 and 'foo')
print('foo' and 3)
print(3 or 'foo')
print('foo' or 3)
print(None or [])

print()

foo = None
bar = 'qux'
is_ok = foo or bar
print(is_ok)

if foo or bar:
    is_ok = True
else:
    is_ok = False
print(is_ok)
# same of above less wordy
is_ok = bool(foo or bar)
print(is_ok)

print()

value = 6

match value:
    case 5:
        print('value is 5')
    case 6:
        print('value is 6')
    case _:  #default case
        print('value is neither 5 nor 6')
# This example is functionally identical to our first if/else statement

print()

value = 10

match value:
    case 1 | 2 | 3 | 4:
        print('value is < 5')
    case 5 | 6:
        print('value is 5 or 6')
    case _:
        print('value is not 1, 2, 3, 4, 5, or 6')  

print()

print('Ternary expressions')
print('value1 if condtion else value2')

#if shape.sides() == 3:
#    print("Triangle")
#else:
#    print("Square")
#print("Triangel" if shape.sides() == 3 else "Square")
print('N/A' if value == None else value)

print()

print('Exercises')
print('#1')

print(False or (True and False)) # False
print(True or (1 + 2))   #True
print((1+2) or True)     #3
print(True and (1+2))    #3
print(False and (1+2))   #False
print((1+2) and True)    #True
print((32*4) >= 129)     #False
print(False != (not True)) #False
print(True == 4)          #False
print(False == (847 == '847')) #True

print()

print('#2')

def even_or_odd(num):
    if num % 2 == 0:
        print('even')
    else:
        print('odd')
even_or_odd(11)
even_or_odd(22)
print('or a ternary expression')
def even_or_odd(num):
    print('even' if num % 2 == 0 else 'odd')
even_or_odd(20)
even_or_odd(11)

print()

print('#3')
def bar_code_scanner(serial):
    match serial:
        case '123':
            print('Product1')
        case '113':
            print('Product2')
        case '142':
            print('Product3')
        case _:
            print('Product no found!')

bar_code_scanner('113')
bar_code_scanner(142)  # integer instead of string

print()

print('#4')
#return ('bar' if foo() else qux())
foo = 2
print('bar' if foo == 2 else 'qux()')
#if foo():
#    return 'bar'
#else:
#    return qux()
if foo == 3:
    print('bar')
else:
    print('qux()')
 
print()

print('#5')
def is_list_empty(my_list):
    if my_list:    # this is truthy
        print('Not Empty')
    else:          # this is falsy
        print('Empty')

is_list_empty([]) # this is falsy so it skips if
is_list_empty([1, 2, 3, 4])# this is truthy
# if empty it is falsy
print()

print('#6')
def caps10(string):
    if len(string) > 10:
        return string.upper()
    else:
        return string

print(caps10('hello world'))
print(caps10('goodbye'))
print(caps10('aburmncatn'))
print(caps10(''))

print()

print('#7')
def num_range(num):
    if num < 0:
        print(f'{num} is less than 0')
    elif num <= 50:
        print(f'{num} is between 0 and 50')
    elif num <= 100:
        print(f'{num} is between 51 and 100')
    else:
        print(f'{num} is greater than 100')

num_range(0)
num_range(25)
num_range(50)
num_range(75)
num_range(100)
num_range(101)
num_range(-1)

