"""Approach #3: Swap the first and last element is using tuple variable. Store the first and last element as a pair
in a tuple variable, say get, and unpack those elements with first and last element in that list. Now, the First and
last values in that list are swapped."""


def swapList(list):
    get = list[-1], list[0]  # Storing the first and last element
    # as a pair in a tuple variable get

    list[0], list[-1] = get  # unpacking those elements
    return list


newList = [12, 35, 9, 56, 24,500]
print(swapList(newList))
