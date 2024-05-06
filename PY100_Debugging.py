def find_first_nonzero_among(numbers):
    for n in numbers:
        if n != 0:
            return n

print(find_first_nonzero_among([0, 0, 1, 0, 2, 0]))
print(find_first_nonzero_among([1]))

print()

import random
def predict_weather():
    sunshine = random.choice([True, False])
    if sunshine:
        print("Today's weather will be sunny!")
    else: 
        print("Today's weather will be cloudy!")
predict_weather()

print()

def multiply_by_five(n):
    return n * 5

print("Hello! Which number would you like to multiply by 5?")
#number = int(input())
number = 10
print(f'The result is {multiply_by_five(number)}!')

print()

pets = {'cat': 'pepe', 'dog': ['sparky', 'fido'], 'fish': 'oscar'}
pets['dog'].append('bowser')
print(pets)

print()

def get_quote(person):
    if person == 'Yoda':
        return 'Do. Or do not. There is no try.'
    if person == 'Confucius':
        return 'I hear and I forget. I see and I remember. I do and I understand.'
    if person == 'Einstein':
        return 'Do not worry about your difficulties in Mathematics. I can assure you mine are still greater.'
print('Confucius says:')
print('"' + get_quote('Confucius') + '"')
print()
print('Yoda says:')
print('"' + get_quote('Yoda') + '"')
print()
print('Einstein says:')
print('"' + get_quote('Einstein') + '"')

print()

numbers = []
for i in range(1, 6):
    numbers.append(i)
print(numbers)
print(list(range(1, 6)))

print()


info = {'name': 'Srdfan', 'age': 38}
print(info.get('city', 'Unknown'))
print(info.get('age', 'Unknown'))
print() # or
if 'city' in info:
    print(info['city'])
else:
    print('Unknown')

if 'name' in info:
    print(info['name'])
else:
    print('Unknown')

print()

sub_list = ["-", "-", "-"]
matrix = []

for _ in range(3):
    #matrix.append(sub_list.copy())
    matrix.append(sub_list[:])
    #matrix.append(list(sub_list))

matrix[0][0] = "X"
matrix[1][0] = "O"
print(matrix)

print()

def find_maximum(numbers):
    if not numbers:
        return None
    max_number = numbers[0] # first element of the list
    #max_number = float('-inf') negative infinity
    for number in numbers:
        if number > max_number:
            max_number = number
    return max_number

print(find_maximum([45, 3, 10, 98, 22]))
print(find_maximum([-1, 0, 5, 3]))
print(find_maximum([-10, -3, -20, -2]))

print()

def digit_product(str_num):
    digits = [int(n) for n in str_num]
    #digits = []
    #for n in str_num:
    #   digits.append(int(n))

    product = 1
    # can not be 0  0 * num will always be 0

    for digit in digits:
        product *= digit
        # product = product * digit
    return product
result = digit_product('12345')
print(result)
print(digit_product('7349'))