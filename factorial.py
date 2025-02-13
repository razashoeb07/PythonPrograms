def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n - 1)


number = int(input("Enter a number : "))
result = factorial(number)
print(f"factorial is : ", result)
# print(f"factorial of {number} is {result}.")
