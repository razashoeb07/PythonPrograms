# Approach 2: The last element of the list can be referred as list[-1]. Therefore, we can simply swap list[0] with
# list[-1].
def swapList(newList):
    newList[0], newList[-1] = newList[-1], newList[0]
    return newList


newList = [12, 35, 9, 56, 24]
print(swapList(newList))

"""
Time Complexity: O(1)
Auxiliary Space: O(n), where n is length of list
"""