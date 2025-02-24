"""Python provides us with various ways of reversing a list. We will go through some of the many techniques on how a
list in Python can be reversed.

Example:

Input: list = [4, 5, 6, 7, 8, 9]
Output: [9, 8, 7, 6, 5, 4]
Explanation: The list we are having in the output is reversed to the list we have in the input.

Below are the approaches that we will cover in this article:

1.Using the slicing technique
2.Reversing list by swapping present and last numbers at a time
3.Using the reversed() and reverse() built-in function
4.Using a two-pointer approach
5.Using the insert() function
6.Using list comprehension
7.Reversing a list using Numpy
-------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------
"""

# mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # 1.Using the slicing technique
# print("before reversing mylist : ", mylist)
#
# mylist2 = mylist[::-1]
# print("after reversing mylist : ", mylist2)

"""
def mylistReversing(mylist1):
    var = mylist1[::-1]
    return var


lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(mylistReversing(lst))

"""

""""
def reverseList(arr):  # 4.Using a two-pointer approach
    left = 0
    right = len(arr) - 1
    while left < right:
        # swap
        temp = arr[left]
        arr[left] = arr[right]
        arr[right] = temp
        left += 1
        right -= 1
    return arr


arr = [10, 20, 30, 40, 50]
print("after reverse list : ", reverseList(arr))
"""

# lst = [1000, 2000, 5000, 7000, 9000]  # 5.Using the insert() function
# blank_list = []
# for i in lst:
#     blank_list.insert(0, i)
# print(blank_list)


