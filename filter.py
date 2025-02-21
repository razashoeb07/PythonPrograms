"""
The Python filter() function is a built-in function that allows you to filter a sequence (e.g., a list, tuple, or set)
based on a given condition. The function takes two arguments – a function and a sequence
"""

"""
Syntax
filter(function, iterable)
● function: A function that tests each element of the iterable. It should return True or
False.
● iterable: The iterable whose elements are to be filtered.

"""

"""
Examples
1. Filtering Even Numbers:
○ Filter out only the even numbers from a list
"""

number = [12, 20, 65, 44, 48, 8]

# def num_even(a):
#     return a % 2 == 0
# return True


# result = filter(lambda a: a % 2 == 0, number)
# print(list(result))
# print(list(result))  # only one time consume

strings = ["hello", "", "world", "python", "", "filter"]
result = filter(lambda s: s != "", strings)
print(list(result))

"""
4. Filtering with None Function:
○ Using None as the function will filter out all elements that are False, None, 0, or
empty.

"""

# values = [0, 1, 2, None, '', 'hello', [], [1, 2], False, True]
# result = filter(None, values)
# print(list(result))

"""
Practical Use Cases
1. Filtering a List of Dictionaries:
○ Filter a list of dictionaries based on a condition.

"""

people = [
    {'name': "Alice", 'age': 25},
    {'name': 'Bob', 'age': 30},
    {'name': 'Charlie', 'age': 35}

]

older_people = filter(lambda person: person['age'] > 25, people)
print(list(older_people))


"""
https://infyspringboard.onwingspan.com/web/en/app/profile/dashboard
"""