# Approach #1: Find the length of the list and simply swap the first element with (n-1)th element.

"""
Examples:

Input : [12, 35, 9, 56, 24]
Output : [24, 35, 9, 56, 12]

Input : [1, 2, 3]
Output : [3, 2, 1]
"""


def swapList(NewList):  # Swap function
    size = len(NewList)

    temp = NewList[0]  # applying the logic of this code..! # Swapping
    NewList[0] = NewList[size - 1]
    NewList[size - 1] = temp
    return NewList


NewList = [12, 35, 9, 56, 24]

# function calling
print((swapList(NewList)))
