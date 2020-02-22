def odd_indices(lst):
    # create empty list
    new_list = []

    # iterate through the list an add every odd index
    for index in range(len(lst)):
        print(index)
        if index % 2 != 0:
            new_list.append(lst[index])
    # return the list
    return new_list
print(odd_indices([4, 3, 7, 10, 11, -2]))

# ----------------------- #

# EXPONENTS
def exponents(bases, powers):
  new_list = []
  for i in range(len(bases)):
    for j in range(len(powers)):
      new_list.append(bases[i]**powers[j])

  return new_list

print('\nEXPONENTS: ')
print(exponents([2, 3, 4], [1, 2, 3]))

# ----------------------- #
# Larger Sum
def larger_sum(lst1, lst2):
    sum_of_first = 0
    sum_of_second = 0

    for val in lst1:
        sum_of_first += val
    for val in lst2:
        sum_of_second += val

    if sum_of_second > sum_of_first:
        return lst2
    return lst1
print(larger_sum([1, 9, 5], [2, 3, 7]))
