# without list Comprehension

# var = []
# for i in range(1, 101):
#    var.append(i)
# print(var)

value = [m for m in range(1, 101)]  # using list Comprehension only two lines
print(value)

# value = [m for m in range(1, 101) if m % 2 == 0]  # using list Comprehension with filtering
# print(value)
