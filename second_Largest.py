def ArrSecondLargestNum(arr):
    if len(arr) < 2:
        raise ValueError("Array must contain at least two distinct elements")

    largest = second_largest = None
    for num in arr:
        if largest is None or num > largest:
            second_largest = largest
            largest = num
        elif num != largest and (second_largest is None or num > second_largest):
            second_largest = num

    if second_largest is None:
        raise ValueError("Array doesn't have distinct largest element..")

    return second_largest


arr = [10, 20, 20, 4, 45, 45, 45, 99, 99]

result = ArrSecondLargestNum(arr)
print(result)
