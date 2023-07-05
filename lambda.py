# a lambda function is a simple expression that return a values
# lambda function can take any number of arguments but can only have one expression
# lambda function cannot contain any statements and cannot be a direct call to print
# lambda function can be used inside list and dictionary
# lambda function can be used inside another function
# lambda function can be used inside another lambda function
# lambda function can be used inside if else statement
# lambda function can be used inside for loop
# lambda function can be used inside while loop
# lambda function can be used inside try except block
# lambda function can be used inside class
# lambda function can be used inside if statement
# lambda function can be used inside elif statement

from functools import reduce


def squared(num): return num * num
# lambda num: num * num


print(squared(5))


def addTwo(num): return num + 2
# lambda num: num + 2


print(addTwo(5))


def sum_total(a, b): return a + b
# lambda a, b: a + b


print(sum_total(5, 6))

#############################################
# lambda function inside inside another fuction


def funcBuilder(x):
    return lambda num: num + x


addFive = funcBuilder(5)
addTwenty = funcBuilder(20)

print(addFive(10))
print(addTwenty(5))

#############################################
# Waht is a higher order function?
# A higher order function is a function that takes another function as an argument or returns another function as a result
# A higher order function can take any number of arguments but can only have one expression
# A higher order function cannot contain any statements and cannot be a direct call to print
# A higher order function can be used inside list and dictionary
# A higher order function can be used inside another function
# A higher order function can be used inside another higher order function

lambda num: num * num
numbers = [10, 2, 3, 4, 5]
squared_nums = list(map(lambda num: num * num, numbers))
print(squared_nums)

# Another ways to write the above code
'''
numbers = [10, 2, 3, 4, 5]
squared_nums = map(lambda num: num * num, numbers)
print(list(squared_nums))
'''

#############################################
# filter function
# filter function takes a function and a list as an argument
# filter function returns a list of values for which the function returns true
# filter function can take any number of arguments but can only have one expression
# filter function cannot contain any statements and cannot be a direct call to print
# filter function can be used inside list and dictionary
# filter function can be used inside another function

lambda num: num % 2 != 0
numbers = [10, 2, 3, 4, 5]
odd_nums = list(filter(lambda num: num % 2 != 0, numbers))
print(odd_nums)

# Another ways to write the above code
'''
odd_nums = filter(lambda num: num % 2 != 0, numbers)
print(list(odd_nums))
'''

#############################################
# Higher order function
lambda acc, curr: acc + curr
numbers = [1, 2, 3, 4, 5, 1]
total = reduce(lambda acc, curr: acc + curr, numbers, 10)
print(total)

print(sum(numbers, 10))
# Another ways to write the above code
'''
numbers = [1, 2, 3, 4, 5, 1]
total = reduce(lambda acc, curr: acc + curr, numbers)
print(total)
'''

#############################################
lambda acc, curr: acc + len(curr)
names = ['James', 'Michael', 'Dave', 'Sarah', 'John', 'Ashley']
char_count = reduce(lambda acc, curr: acc + len(curr), names, 0)
print(char_count)
