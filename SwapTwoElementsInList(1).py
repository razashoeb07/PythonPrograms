"""
Input : List = [23, 65, 19, 90], pos1 = 1, pos2 = 3
Output : [19, 65, 23, 90]

Input : List = [1, 2, 3, 4, 5], pos1 = 2, pos2 = 5
Output : [1, 5, 3, 4, 2]
"""

mylist = [23, 65, 19, 90]
print("Original List : ", mylist)
pos1, pos2 = 1, 3
mylist[pos1], mylist[pos2] = mylist[pos2], mylist[pos1]

print("After Swapping with specific locations : ", mylist)




