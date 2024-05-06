car = {
    'type':     'sedan',
    'color':    'blue',
    'mileage':  80_000,
    'year':     2003,
}

print(car)
print()
car['year'] = 2003
del car['mileage']
print(car)
print()
print(car['color'])
print(car.get('color'))
print(car.get('mileage', 0))
print(len(car))

print()

student = {
    'id':     123,
    'grade':  'B',
}
print(student.get('name'))
print(student.get('grade'))
print('name' in student)
print('grade' in student)

print()

vehical = {
    'car': {
        'type':    'sedan',
        'color':   'blue',
        'year':    2003,
    },
    'truck': {
        'type':    'pickup',
        'color':   'red',
        'year':    1998,
    },
}
print(vehical)
print(vehical['truck'])

print()

car = [
    ['type', 'sedan'],
    ['color', 'blue'],
    ['year', 2003],
]

print()

numbers = {
    'high':   100,
    'medium': 50,
    'low':    25,
}
half_numbers = []
for num in numbers.values():
    half_numbers.append(num // 2)

print(half_numbers)

print()
print(numbers.items())
print()
for key in numbers:
    print(key)
    numbers[key]
print()
for pair in numbers.items():
    print(pair)
print()
for key, value in numbers.items():
    print(f'A {key} number is {value}.')