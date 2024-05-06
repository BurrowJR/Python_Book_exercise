num = 3
my_list = [1, 2, 3]
my_dict = {
    'a': 1,
    'b': 2,
}
print('first assignment of num', num)
print('first assignment my_list', my_list)
print('first assignment my_dict', my_dict)

num = 42
print('num reassigned', num)
my_list[1] = 42
my_dict['b'] = 3
print('reassignment of element, my_list mutated', my_list)
print('reassignment of dictionary pair, mutated my_dict', my_dict)

my_list = (2, 3, 4)
my_dict = {'x': 0}
print('reassign my_list', my_list)
print('reassign my_dict', my_dict)
print()
print('Variable Exercises')
print('#1')
# idnex        idiomatic
#CatName       non-idiomatic   cat_name
#lazy_dog      idiomatic
#quick_Fox     non-idiomatic   quick_fox
#1stCharacter  illegal         first_character
#operand2      idiomatic
#BIG_NUMBER    non-idiomatic   big_number
#π             non_idiomatic   pi
print()
print('#2')
#function and variable names follow the same convension rules   These answers are the same as above.
print()
print('#3')
#index      non-idiomatic   INDEX
#CatName    non-idiomatic   CATNAME
#snake_case non-idiomatic   SNAKE_CASE
#LAZY_DOG3  idiomatic
#1st        illegal         FIRST
#operand2   non-idiomatic   OPERAND2
#BIG_NUMBER idiomatic
#π          non-idiomatic   PI
print()
print('#4')
#index        non-idiomatic     Index
#CatName      idiomatic
#Lazy_Dog     non-idiomatic     LazyDog
#1st          illegal           First
#operand2     non-idiomatic     Operand2
#BigNumber3   idiomatic
#∏i           non-idiomatic     Not an ASCII
print()
print('#5')
greeter = 'Victor'
print(f'Good Morning, {greeter}.')
print(f'Good Afternoon, {greeter}.')
print(f'Good Evening, {greeter}.')
print()
print('#6')
age = 22
print(f'You are {age} years old.')
print(f'In 10 years, you will be {age + 10} years old.')
print(f'In 20 years, you will be {age + 20} years old.')
print(f'In 30 years, you will be {age + 30} years old.')
print(f'In 40 years, you will be {age + 40} years old.')
print()
print('#7')
NAME = 'Victor'
print('Good Morning, ' + NAME)
print('Good Afternoon, ' + NAME)
print('Good Evening, ' + NAME)
print()# This runs just fine but NAME is a variable not a constant so it should be lower case.
NAME = 'Nina'
print('Good Morning, ' + NAME)
print('Good Afternoon, ' + NAME)
print('Good Evening, ' + NAME)
print()
print('#8')
balance = 1000
years = 5
interest_per_year = 1.05
print(f'In {years} years your balance will be {balance * interest_per_year * interest_per_year * interest_per_year * interest_per_year * interest_per_year}.')
print()
print('#9')
balance *= interest_per_year
print(balance)
balance *= interest_per_year
print(balance)
balance *= interest_per_year
print(balance)
balance *= interest_per_year
print(balance)
balance *= interest_per_year
print(balance)
print()
print('#9')
obj = 42
print(obj)
obj = 'ABcd' # not mutate / Reassign
print(obj)
print(obj.upper()) # not mutate
print(obj)
obj = obj.lower() # not mutate / Reassign
print(obj)
print(len(obj)) # not mutate
obj = list(obj) # not mutate / Reassign
print(obj)
print(obj.pop()) # mutate
print(obj)
obj[2] = 'X'  # mutate
print(obj)
print(obj.sort())  # mutate
print(obj)
print(set(obj))  # not mutate
print(obj)
obj = tuple(obj) # not mutate / Reassign
print(obj)