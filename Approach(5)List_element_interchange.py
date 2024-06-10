def swapList(List):
    if len(List) >= 2:
        result = List[-1:] + List[1:-1] + List[:1]
        return result


inp = [12, 35, 9, 56, 24]

print("printing the original List : ", inp)

print("after the swapping first and last element : ", swapList(inp))  # calling function
