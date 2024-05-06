import random
random_number = random.randint(0, 1)
print(random_number)
if random_number == 1:
    print('Yes!')
else:
    print('No!')
print()
print('ternary expression')
print('Yes!' if random_number else 'No!')

print()

weather = ['sunny', 'rainy', 'windy']
weather = 'windy'
if weather == 'sunny':
    print("It's a beautiful day!")
elif weather == 'rainy':
    print('Grab your umbrella')
else:
    print("Let's stay inside.")
          
print()
animal = 'horse'
match animal:
    case 'duck':
        print('quack')
    case 'squirrel':
        print('nook nook')
    case 'horse':
        print('neigh')
    case 'bird':
        print('tweet tweet')
    case _:
        print('*cricker*')
print()
weather = 'foggy'
match weather:
    case 'sunny':
        print("It's a beautiful day!")
    case 'rainy':
        print("Grab your umbrells")
    case 'windy':
        print('Hang on to your hat!')
    case 'snowy':
        print('Grab the sled!')
    case 'blizzard':
        print("Let's say inside!")
    case _:
        print("Let's read a book!")

print()
if False or True:
    print('Yes!')
else:
    print('No...')
print()

sale = True
admission_price = 5.25 if not sale else 3.99
print(f'{admission_price}')
print()
speed = 0
acceleration = 24
braking_force = 19
is_moving = braking_force < acceleration and (speed > 0 or acceleration > 0)
print(is_moving)
