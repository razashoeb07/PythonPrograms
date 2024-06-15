# Approach 2 Using inbuilt list.pop() function
mylist = [23, 65, 19, 90]  # index start from Zero (0)
pos1, pos2 = 1, 3

print("Original List : ", mylist)

first = mylist.pop(pos1)
second = mylist.pop(pos2 - 1)
mylist.insert(pos2, first)
mylist.insert(pos1, second)

print("After Swapping with specific locations : ", mylist)
