# tuples are like lists
my_tuple = ('Oranges', 'Milk', 32, 'Lactaid')
my_list = ['Oranges', 'Milk', 32, 'Lactaid']

# same result inside
print(my_tuple)
print(my_list)

# I just CANNOT change what's in a tuple -- tupels are immutable lists
# I can 'unpack' a tuple, however
first_item, second_item, third_item, fourth_item = my_tuple

# The items have been 'unpacked'
print(first_item)
print(second_item)
print(third_item)
print(fourth_item)

# parenthesis around a single-item tuple will result in a single item and NOT a tuple
my_crappy_fake_tuple = ('Nik')
print(my_crappy_fake_tuple)

# we NEED to put a comma after the first element -- use a 'trailing' comma
my_actual_tuple = ('Nik',)
print(my_actual_tuple)
