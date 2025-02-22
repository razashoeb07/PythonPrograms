names = ['Saif', 'Dilshad', 'Raza']

# def length_names(n):
#     return n, len(n)
# 
# 
# map_object = map(length_names, names)
# # print(list(map_object))
# for i in map_object:
#     print(i)


numbers = [1, 2, 3, 4]


def even_odd(numbers):
    if numbers % 2 != 0:
        s = numbers * numbers
        return s
    else:
        return numbers


result = map(even_odd, numbers)
print(list(result))
