txt1 = 'Hello, {name}. You are a {proffession}.'.format(name = "Victor", proffession = "programmer")
print(txt1)
txt2 = "My name is {0}, I'm {1}.".format("John", 36)
print(txt2)
txt3 = "Hello, {}. You are a {}.".format("Amy", "programmer")
print(txt3)
txt4 = "Hello, my name is {}."
print(txt4.format("Johnna"))
name = "Victor"
profession = "programmer"
txt5 = "Hello, {}. You are a {}."
txt6 = txt5.format(name, profession)
print(txt6)
txt7 = f'Hello, {name}. You are a {profession}.'
print(txt7)

print()
ice_cream_density = 10
while ice_cream_density > 0:
    print('Drip...')
    ice_cream_density -= 1
print('The ice cream melted.')

print()
# power_operator = **   Do This First
# Second multiply, divide, and modulo
# Third add, subtract
# 4*5 + 9/10 = 20 + .9 = 20.9
print(4 * 5 + 3 ** 2 / 10)
use_parentheses = (4 * 5) + ((3**2) / 10)
# easier to read and avoids mistakes
print()

import datetime
x = datetime.datetime.now()
print(x)

print(f'Today is {x}.')
print(x.strftime("%B %d, %Y %I:%M"))
print(x.strftime("%x %X"))
print(x.strftime("It is week %U, day %j of %Y"))
print(x.strftime("%c"))
print(x.year)
print(x.strftime("%A"))

y = datetime.datetime(2012, 6, 25)
print(y.strftime("%B, %A"))

print()
from datetime import date
today = date.today()
print(today)

today_year = today.year
print(today_year)

print(today.isocalendar())
iso_year = today.isocalendar()[0]
print(iso_year)

xmas = date(2024, 12, 25)
anastasia_b_day = date(2024, 6, 25)
print(f'There are {xmas-today} days till Christmas!')
print(f'Anastasia will be {today_year - 2012} years old this year and there is {anastasia_b_day - today} days till her birthday!')

print()
separator = '-'
names = ['Bob', 'Jo', 'Kim']
result = separator.join(names)
print(result)

#print(separator.join())
#TypeError: str.join() takes exactly one argument (0 given)

#print(separator.join('Bob', 'Jo'))
#TypeError: str.join() takes exactly one argument (2 given)

print()

string = "Hello, World!"
print("World" in string)
print("Python" in string)

print()
speed_limit = 60
current_speed = 80
if current_speed > speed_limit:
    print('"People are so bad at driving cars that computers don\'t have to be that good to be much better." -- Marc Andreessen')

    print()
    tweet = 'Woohoo! :-)'
    if len(tweet) > 140:
        print('Tweet is too long!')
    length_of_tweet = len(tweet + str(5))
    print(length_of_tweet)