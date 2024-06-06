def swapList(List):
    first = List.pop(0)
    last = List.pop(-1)
    
    List.insert(0, last)
    List.insert(-1, first)
    return List


newList = [12, 9, 35, 56, 24]
print(swapList(newList))
