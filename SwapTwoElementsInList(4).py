def SwapPositions(list, pos1, pos2):
    for i, x in enumerate(list):
        if i == pos1:
            element1 = x
        if i == pos2:
            element2 = x
    list[pos1] = element2
    list[pos2] = element1
    return list


List = [23, 65, 19, 90]
pos1, pos2 = 1, 3

print("Original List : ", List)
print("After Swapping with specific locations : ", SwapPositions(List, pos1 - 1, pos2 - 1))