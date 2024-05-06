for num in range(0, 11, 2): # range(start, stop, step)  
    print(num)

print()

for i in range(10, 0, -1):
    print(i)
print('Launch!')

print()

greeting = 'Aloha!'
count = 1

while count <= 3:
    print(greeting)
    count += 1

print()

for _ in range(3):
    print(greeting)

print()

for num in range(1, 101):
    print(num * 2)

print()

lst = [1, 3, 7, 15]
index = 0

while index < len(lst):
    print(lst[index])
    index += 1

print()

friends = ['Sarah', 'John', 'Hannah', 'Dave']
for friend in friends:
    print(f'Hello, {friend}!')

print()

cities = ['Istanbul', 'Los Angeles', 'Tokyo', None, 'Vienna', None, 'London', 'Beijing', None]

for city in cities:
    if city == None:
        continue
    print(len(city), city)

print()

while True:
    print("and on")
    break

print()

fish_list = ['Dory', 'Marlin', 'Gill', 'Nemo', 'Bruce']
for fish in fish_list:
    print(fish)
    if fish == 'Nemo':
       break

print()

i = 0
while True:
    name = fish_list[i]
    print(name)
    if name == 'Nemo':
        break
    i += 1

print()

while True:
    print('Should I stop looping? yes or no')
    answer = input()
    if answer == 'yes':
        break
    print('Please!!')