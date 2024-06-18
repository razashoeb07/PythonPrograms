# Approach 3 Using tuple method

mylist = [23, 65, 19, 90]
pos1, pos2 = 1, 3

print("Original List : ", mylist)

get = (mylist[pos1], mylist[pos2])
mylist[pos2], mylist[pos1] = get

print("After Swapping with specific locations : ", mylist)
