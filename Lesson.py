
import math
from enum import Enum


# print(RPS(2))
# print(RPS.ROCK)
# print(RPS['ROCK'])
# print(RPS.ROCK.value)
# sys.exit()

line01 = "********************"
line02 = "*                  *"
line03 = "*    WELCOME!      *"
line04 = "********"

# starts with a blank line
print(' ')
print(line01)
print(line02)
print(line03)
print(line02)
print(line01)
############################ OPERATOR ###################################
# Comparison Operators(1st IF statment)
meaning = 42
print('')

# if meaning > 10:
#     print('Right on!')
# else:
#     print('Not Today')
# Ternary Operator
print('Right On!') if meaning > 10 else print('Not Today')

############################## DATA TYPES############################
# String data type

# Literal assignment
first = "Dave"
Last = "Grey"

# print(type(first))
# print(type(first) == str)
# print(isinstance(first, str))

# Constructor Fuction
# pizza = str('Pepperoni')
# print(type(pizza))
# print(type(pizza) == str)
# print(isinstance(pizza, str))

# Concatenation
fullname = first + '' + Last
print(fullname)

fullname += '!'
print(fullname)

# Casting a number to a string
decade = str(1980)
print(type(decade))
print(decade)

statement = 'I like rock music from the ' + decade + 's.'
print(statement)

# Multiple lines Casting
multiline = '''
Hey, how are you?                          

I was just checking in.                      
                                All good?

'''
print(multiline)

# Escaping special characters
sentence = 'I\'m back at work!\tHey!\n\nWhere\'s this at\\located?'
print(sentence)

# String methods
print(first)
print(first.lower())
print(first.upper())
print(first)

print(multiline.title())
print(multiline.replace("good", 'ok'))
print(multiline)

print(len(multiline))
multiline += '                                            '
multiline = '                ' + multiline
print(len(multiline))
print(len(multiline.strip()))
print(len(multiline.lstrip()))
print(len(multiline.rstrip()))
print("")

# Build a menu
title = "menu".upper()
print(title.center(20, '='))
print("Coffee".ljust(16, '-') + '$1'.rjust(4))
print("Muffin".ljust(16, '-') + '$3'.rjust(4))
print("Cheesecake".ljust(16, '-') + '$4'.rjust(4))
print('')

# string index values
print(first[1])
print(first[-1])
print(first[1:-1])
print(first[1:])

# Some method return boolean data
print(first.startswith('D'))
print(first.endswith('Z'))

# Boolean data type (Constructor Function)
myValue = True
x = bool(False)
print(type(x))
print(isinstance(myValue, bool))
print('')
# Numeric data types

# integer types
price = 100
best_price = int(80)
print(type(price))
print(isinstance(best_price, int))

# Float type
gpa = 3.28
y = float(1.14)
print(type(gpa))

# Complex type
comp_value = 5+3j
print(type(comp_value))
print(comp_value.real)
print(comp_value.imag)

# Built-in fuctions for numbers
print(abs(gpa))
print(abs(gpa * -1))
print(round(gpa))
print(round(gpa, 1))
print('')

print(math.pi)
print(math.sqrt(64))
print(math.ceil(gpa))
print(math.floor(gpa))
print('')

# Casting a string to a number
zipcode = '10001'
zip_value = int(zipcode)
print(type(zip_value))

# Error if you attempt to cast incorrect
# zip_value = int('New York)

############################## LIST & TUPLES##############################
# Valid List
users = ['Dave', 'Grey', 'John']
data = ['Grey', 48, 'Dave']
emptyList = []

print('Dave' in users)
print(users[0])
print(users[-2])

print(users.index('John'))

print(users[0:2])
print(users[1:])
print(users[-3:-1])

print(len(data))

# Add Item
users.append('Elsa')
print(users)

users += ['Jason']
print(users)

users.extend(['Jimmy', 'Sarah'])
print(users)

# users.extend(data)
# print(users)
users.insert(0, 'Bob')
print(users)

users[2:2] = ['Eddie', 'Alex']
print(users)

# Replace Values
users[1:3] = ['Robert', 'Eric']
print(users)

users.remove('Bob')
print(users)

print(users.pop())
print(users)

# del users[0]
data.clear()
print(data)

users[1:2] = ['dave']
users.sort()
print(users)

# Alphabetical order
users.sort(key=str.lower)
print(users)

nums = [4, 48, 73, 3, 1]  # Assending
nums.reverse()
print(nums)

# nums.sort(reverse=True)#desending
# print(nums)

print(sorted(nums, reverse=True))
print(nums)

numscopy = nums.copy()
mynums = list(nums)
mycopy = nums[:]

print(numscopy)
print(mynums)
mycopy.sort()
print(mycopy)
print(nums)

myList = list([1, 'John', True])
print(myList)

# Tuples
myTuple = tuple(('Dave', 74, True))

anotherTuple = (1, 25, 32, 47, 25, 25)
print(tuple)
print(type(myTuple))
print(anotherTuple)

newList = list(myTuple)
newList.append('Neil')
newtuple = tuple(newList)
print(newtuple)

(one, *two, hey) = anotherTuple
print(one)
print(two)
print(hey)

print(anotherTuple.count(25))

###################### >>SETS AND DICTIONARIES<<##########################
# Dictionaries
band = {
    'vocals': 'plant',
    'guiter': 'page'
}

band2 = dict(vocals='plant', guiter='page')
print(band)
print(band2)
print(type(band))
print(len(band))

# Access items
print(band['vocals'])
print(band.get('guiter'))

# list all keys
print(band.keys())

# list all values
print(band.values())

# list of keys/value pairs as tuples
print(band.items())

# verify a key exists
print('guiter' in band)
print('triangle' in band)

# change values
band['vocals'] = 'coverdale'
band.update({'bass': 'JPJ'})
print(band)

# Remove items
print(band.pop('bass'))
print(band)

band['Drums'] = 'Bomham'
print(band)

print(band.popitem())  # Tuple
print(band)

# Delete and Clear
band['Drums'] = 'Bomham'
del band['Drums']
print(band)

band2.clear()
print(band2)

del band2

# Copy dictionaries
band2 = band.copy()
band2['Drums'] = 'Thunder'
print('Good copy!')
print(band)
print(band2)

# or use the dic() constructor function
band3 = dict(band)
print('Good copy!')
print(band)
print(band3)
print('')

# Nested dictionaries
member1 = {
    'name': 'Plant',
    'instrument': 'guiter'
}
member2 = {
    'name': 'Page',
    'instrument': 'Vocals'
}
band = {
    'member1': member1,
    'member2': member2
}
print(band)
print(band['member1']['name'])

# Sets
nums = {1, 2, 3, 4, 5}

nums2 = set((1, 2, 3, 4, 5))
print(nums)
print(nums2)
print(type(nums))
print(len(nums))

# No duplicte allowed
nums = {1, 2, 3, 3, 4}
print(nums)

# True is a dupe of 1, False is a dupe of zero
nums = {1, True, 2, False, 3, 4, 0}
print(nums)

# Check if a value is in a set
print(2 in nums)

# But you cannot refer to an element in the set with an index position or a keu
# Add a new element to a set
nums.add(8)
print(nums)

# Add elements fron one set to another
morenums = {5, 6, 7}
nums.update(morenums)
print(nums)

# We can use updates with list, Tuples, and dictionaries too.

# merge two set to create a new set
one = {1, 2, 3, 4}
two = {5, 6, 7, 8}

mynewset = one.union(two)
print(mynewset)

# keep only the duplicates
one = {1, 2, 3, 4}
two = {3, 6, 2, 8}

one.intersection_update(two)
print(one)

# keep everything except the duplicates
one = {1, 2, 3, 4}
two = {3, 6, 2, 8}

one.symmetric_difference_update(two)
print(one)

############################# While Loop & For Loop ##########################
# WHILE LOOP
value = 1
# while value <= 10:
#     print(value)
#     if value == 5:
#         break
#     value += 1


# while value <= 10:
#     value += 1
#     if value == 5:
#         continue
#     print(value)
# else:
#     print("value is now equal to " + str(value))

# FOR LOOP
name = ["Dave", "Sara", "John"]
# for x in name:
#     print(x)

# for x in name:
#     if x == "sarah":
#         break
#     print(x)

# for x in name:
#     if x == "sarah":
#         continue
#     print(x)

# for x in range(3, 5):
#     print(x)

for x in range(0, 101, 5):
    print(x)
else:
    print("Good that\'s over!")

# Loop to two different list
names = ["Dave", "Sara", "John"]
actions = ["Code", "Eat", "Sleep"]

# for name in names:
#     for action in actions:
#         print(name + " " + action + ".")

for action in actions:
    for name in names:
        print(name + " " + action + ".")

######################### FUNCTIONS ################################


def hello_function():
    print("Hello World!")


hello_function()


def sum(num1, num2):
    return num1 + num2


total = sum(2, 3)
print(total)


def sum(num3, num4):
    if (type(num3) is not int or type(num4) is not int):
        return 0
    return num3 + num4


total = sum(3, 4)
print(total)


def multiple_items(*args):
    print(args)
    print(type(args))


multiple_items("Dave", "Sara", "john")


def mult_name_item(**kwargs):
    print(kwargs)
    print(type(kwargs))


mult_name_item(first="Dave", last="Grey")

########################### RECURSION #################################
# Recursion in python happen when a function calls itself(Reursive func)


def add_one(num):

    if (num >= 9):
        return num + 1

    total = num + 1
    print(total)

    return add_one(total)


# we call(add_one(0))and it return 9
mynewtotal = add_one(0)
print(mynewtotal)  # it return the num 10

# While Loop
count = 0

while value:
    count += 1
    print(count)
    if (count == 5):
        break
    else:
        value = 0
        continue

########################## SCOPE ####################################
# global scope( it has access outside the function)
name = "Dave"
count = 1


# def greetings(firstname):
#     # Local scope(it can not be access outside of the function)
#     color = "Green"
#     print(color)
#     print(name)
#     print(firstname)

# greetings has been called inside the local scope of another
# greetings("john")

# Parent funcetion
def another():
    # Local scope(it can not be access outside of the function)
    color = "Green"
    global count
    count += 1
    print(count)

    # nested funtion
    def greetings(firstname):
        nonlocal color
        color = "red"
        print(color)
        print(firstname)

    greetings("Mark")


another()

################################ CLOSURE ################################
# Closure is a function having access to the scope of its parent
# function after the parent function has returned


def parent_function(person):
    coins = 3

    def play_game():
        nonlocal coins
        coins -= 1

        if coins > 1:
            print('\n' + person + ' has ' + str(coins) + ' coins left. ')
        elif coins == 1:
            print('\n' + person + ' has ' + str(coins) + ' coin left. ')
        else:
            print('\n' + person + ' is out of coin. ')
    return play_game


tommy = parent_function('Tommy')
jenny = parent_function('Jenny')

tommy()
tommy()

jenny()

################################ F_Strings #####################################
person = "Dave"
coins = 3

print("\n" + person + " has " + str(coins) + " coins left")
# Using percent S(%s) to call the function
message = "\n%s has %s coins left." % (person, coins)
print(message)

# Using the FORMAT method to call the function
message = "\n{} has {} coins left.".format(person, coins)
print(message)

# Using the INDEX method inside the FORMAT method
message = "\n{1} has {0} coins left.".format(coins, person)
print(message)
# Asigning the FORMAT method by name
message = "\n{person} has {coins} coins left.".format(
    coins=coins, person=person)
print(message)
# FORMAT whit Dictionaries
player = {'person': 'Dave', 'coins': 3}

message = "\n{person} has {coins} coins left.".format(**player)
print(message)

################################
# f-Stirngs!
message = f"\n{person} has {coins} coins left."
print(message)
# Use Multiply with f-string
message = f"\n{person} has {2 * 5} coins left."
print(message)
# Use Method inside the f-string
message = f"\n{person.lower()} has {2 * 5} coins left."
print(message)

message = f"\n{player['person']} has {2 * 5} coins left."
print(message)

##############################
# we can pass formatting OPTION into f-String

num = 10
print(f"\n2.25 times {num} is {2.25 * num:.2f}\n")
# LOOP formatting Options
for num in range(1, 11):
    print(f"\n2.25 times {num} is {2.25 * num:.2f}\n")

for num in range(1, 11):
    print(f"{num} divided by 4.52 is {num/ 4.52:.2%}")
