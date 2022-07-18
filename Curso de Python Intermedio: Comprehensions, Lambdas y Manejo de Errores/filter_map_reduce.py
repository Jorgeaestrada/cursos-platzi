from functools import reduce


filter_number_list1 = [1, 4, 5, 6, 9, 13, 19, 21]


# filter
odd = list(filter(lambda x: x % 2 != 0, filter_number_list1))

print(odd)

# map
map_number_list = [1, 2, 3, 4, 5]

square = list(map(lambda x: x**2, map_number_list))

print(square)

# reduce
reduce_number_list = [2, 2, 2, 2, 2]

multiply = list(reduce(lambda a, b: a * b, reduce_number_list))
#print(multiply)
