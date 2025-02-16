
num = int(input("Enter a number : "))
while num >= 10:
    if num % 2 != 0:
        num = (num // 2)
    elif num % 2 == 0:
        num = (num - 2) // 2
else:
    print(num)
