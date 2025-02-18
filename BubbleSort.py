aList = [15, 6, 13, 22, 3, 52, 2]
print("Original List : ", aList)
n = len(aList)
for i in range(n):
    for j in range(0, n - i - 1):
        if aList[j] > aList[j + 1]:
            aList[j], aList[j + 1] = aList[j + 1], aList[j]
print("List After Sorting : ", aList)

# Time Complexity -> O(n^2)
# Space Complexity > 0(1) Inplace Changing
