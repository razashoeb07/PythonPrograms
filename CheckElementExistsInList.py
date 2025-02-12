"""
Check if an element exists in a list in Python
Using “in” Statement
Using a loop
Using any() function
Using count() function
Using sort with bisect_left and set()
Using find() method
Using Counter() function
Using try-except block


Input: test_list = [1, 6, 3, 5, 3, 4]
      Let's suppose  3  # Check if 3 exist or not.
Output: True
Explanation: The output is True because the element we are looking is exist in the list.

"""
"""

var = []
for i in range(1,11):
    var.append(i)
print(var)
#mylist = [1, 2, 3, 4, 5, 6, 7, 8]
# x = 9
y = int(input("enter a number you want to search in your given list : "))
if y in mylist:
    print("yes", y, "is exist in your given list...Thank You.")
else:
    print("oh....Sorry!!", y, "is not exist in your given list.")
"""

while True:

    lst = []
    x = int(input("enter how many element insert in list : "))
    print("enter", x, "element")

    for i in range(1, x+1):
        y = int(input())
        lst.append(y)
    print(lst)
    z = int(input("enter element you want to be search : "))
    if z in lst:
        print("yes", z, "is exist in list..Thank You..!!")
    else:
        print("No..! Sorry", z, "is not exist.")

    user_input = input("Do you want to continue? (yes/no): ")
    if user_input.lower() in ["yes", "y"]:
        print("Continuing...")
    elif user_input.lower() in ["no", "n"]:
        print("Exiting...")
        break
    else:
        while user_input.lower() not in ("no", "n"):
            user_input = input("Invalid input. Please enter yes/no.")
