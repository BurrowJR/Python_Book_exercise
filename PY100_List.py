def first(lst):
    if lst:
        return lst[0]
    else:
        return None

print(first(['Earth', 'Moon', 'Mars']))
print(first([]))

print()

def last(lst):
    if lst:
        return lst[-1]
    else:
        return None

print(last(['Earth', 'Moon', 'Mars']))
print(last([]))

print()

energy = ['fossil', 'solar', 'wind', 'tidal', 'fusion']
print(energy)
energy.remove('fossil')
energy.append('geothermal')
print(energy)

print()

alphabet = 'abcdefghijklmnopqrstuvwxyz'
print(list(alphabet))
print(alphabet)

print()

scores = [96, 47, 113, 89, 199, 102]
count = 0
for scores in scores:
    if scores >= 100:
        count += 1
print(count)

scores = [96, 47, 113, 89, 100, 102]
print(scores)
print()
count = [score for score in scores if score >= 100]
print(count)
print(len(count))

print()

vocabulary = [
    ['happy', 'cheerful', 'merry', 'glad'],
    ['tired', 'sleepy', 'fatigued', 'drained'],
    ['excited', 'eager', 'enthused', 'animated']
]
for synonyms in vocabulary:
    for word in synonyms:
        print(word)

print()

list1 = [2, 6, 4]
list2 = [2, 6, 4]
print(list1 == list2)  # same value
print(list1 is list2)  # not the same place in memory
list3 = list1
print(list3 == list1)
print(list3 is list1)

print()

some_value1 = [0, 1, 0, 0, 1]
some_value2 = 'I leave you my Kingdom, take good care of it.'
print(type(some_value1))
print(type(some_value2))
print(isinstance(some_value1, list))
print(isinstance(some_value2, list))

print()
destinations = ['Prague', 'Lodon' 'Sydney', 'Belfast', 'Rome', 'Aruba', 'Paris', 'Bora Bora', 'Barcelona', 'Rio do Janeiro', 'Marrakesh', 'New York City']
print('for loop')
def contains(element, lst):
    for item in lst:
        if item == element:
            return True
    return False
print(contains('Barcelona', destinations))
print(contains('Nashville', destinations))
print()
print('while loop')
def contains(element, lst):
    index = 0 
    while index < len(lst):
        if lst[index] == element:
            return True
        index += 1
    return False

print(contains('Rome', destinations))
print(contains('Amarillo', destinations))

print()
print('in operator')
def contains(element, lst):
    return element in lst

print(contains('Paris', destinations))
print(contains('Lubbuck', destinations))

print()

passcode = ['11', 'jZ5', 'hQ3f*', '8!7g3', 'p3Fs']
print('-'.join(passcode))

joined_passcode = ''
for i in range(len(passcode)):
    if i > 0:
        joined_passcode += '-'
    joined_passcode += passcode[i]
print(joined_passcode)

print()

grocery_list = ['paprika', 'tofu', 'garlic', 'quinoa', 'carrots', 'broccoli', 'hummus']
while grocery_list:
    checked_item = grocery_list.pop(0)
    print(checked_item)
print(grocery_list)
