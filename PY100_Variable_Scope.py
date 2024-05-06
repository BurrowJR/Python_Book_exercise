if True:   # if False gives an error
    my_value = 20
print(my_value)
print()
x = 10  # is out of scope here
def my_function():
    global x  # have to use global to have access to the outer scope
    x = x + 5
    print(x)
my_function()
print()
def my_function():
    a = 1
    if True:        # if False no output
        print(a)
my_function()
print()
a = 1
def my_function():
    print(a)       # can reference a but can not make any changes
my_function()
print()
a = 1
def my_function():
    a = 2
    print(a)
    # a = 2 must reasign variable before print
my_function()
print()
a = 1
def my_function():
    a = 2
    print(a)
my_function()
print(a)
print()
a = 1
def my_function():
    global a
    a = 2
my_function()
print(a)
print()
greeting = "Hello world!"
print(greeting) # must define greeting before using it
print()
a = 7
def my_function(b):
    b += 10
    print(b)
my_function(a)
print(a)
print()
b = [1, 2, 3]
def my_function():
    b[0] = 10
    print(b)
my_function()
print(b)