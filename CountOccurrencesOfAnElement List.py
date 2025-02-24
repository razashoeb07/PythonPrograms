"""
Given a list in Python and a number x, count the number of occurrences of x in the given list.

Examples:

Input: lst = [15, 6, 7, 10, 12, 20, 10, 28, 10], x = 10
Output: 3
Explanation: 10 appears three times in given list.
Input: lst = [8, 6, 8, 10, 8, 20, 10, 8, 8], x = 16
Output: 0
Explanation: 16 appears zero times in given list.
"""

# Approach Using Loop

# mylist = [10, 20, 30, 10, 40, 10, 40, 50, 40, 20, 10, 50, 60, 90, 60]
# x = 50
# count = 0
# for i in mylist:
#     if i == x:
#         count = count + 1
# print("{} has occurred {} times".format(x, count))
# print(x, "has occurred", count, "times")

# Approach 2 count method

# mylist = [10, 20, 30, 10, 40, 10, 40, 50, 40, 20, 10, 50, 60, 90, 60]
# x = 10
# print("{} has occurred {} times".format(x, mylist.count(x)))

# Approach 3 Using Counter()

from collections import Counter
mylist = [10, 20, 30, 10, 40, 10, 40, 50, 40, 20, 10, 50, 60, 90, 60]
x = int(input("Enter a number that you want to see how many times that number is repeated in the list: "))
dic = Counter(mylist)  # as a dictionary {10:4, 20:2, 30:1, 40:3, 50:2, 60:2, 90:1 }
print("{} has occurred {} times".format(x, dic[x]))
