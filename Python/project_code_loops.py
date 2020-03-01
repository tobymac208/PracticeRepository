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


# ------------------------- #
# Over 9000
def over_nine_thousand(lst):
  sum = 0
  for i in range(len(lst)):
    sum += lst[i]

    if sum > 9000:
      break
  return sum

print(over_nine_thousand([8000, 900, 120, 5000]))

# ---------------------- #
# Largest num
def max_num(nums):
  largest_num = 0

  if not(len(nums) > 0):
    return 0

  largest_num = nums[0]
  for val in nums:
    if largest_num < val:
      largest_num = val
  return largest_num

#Uncomment the line below when your function is done
print(max_num([50, -10, 0, 75, 20]))

# ----------------------- #
# Same Values
def same_values(lst1, lst2):
  list_of_matching_indices = []

  for i in range(len(lst1)):
    if lst1[i] == lst2[i]:
      list_of_matching_indices.append(i)
  return list_of_matching_indices

#Uncomment the line below when your function is done
print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))

# ------------------ #
# Reversed list
def reversed_list(lst1, lst2):
  reversed_list_of_two = []

  for i in range(len(lst2)):
    reversed_list_of_two.append(lst2[-1])
    del lst2[-1]

  for i in range(len(lst1)):
    if reversed_list_of_two[i] != lst1[i]:
      return False
  print(reversed_list_of_two)
  print(lst1)
  return True

#Uncomment the lines below when your function is done
print(reversed_list([1, 2, 3], [3, 2, 1]))
print(reversed_list([1, 5, 3], [3, 2, 1]))
