# 1: Append Sum

#Write your function here
def append_sum(lst):
    # add the last two items of the list together
    for i in range(0, 3):
        # perform this three times
        last_two_together = lst[-2] + lst[-1]
        lst.append(last_two_together)
    return lst

#Uncomment the line below when your function is done
print(append_sum([1, 1, 2]))

# ------------------------------#

# 2: Larger list
def larger_list(lst1, lst2):
    count_list_one = len(lst1)
    count_list_two = len(lst2)

    # does the second list just have more elements?
    if count_list_two > count_list_one:
        return lst2[-1]

    # they either have the same amount of elements or lst1 had more
    return lst1[-1]
print(larger_list([4, 10, 2, 5], [-10, 2, 5, 10]))

# ------------------------------#

# 3: More Than N:
def more_than_n(lst, item, n):
    # check if the certain 'item' appeats in the lst 'n' times
    if lst.count(item) > n:
        return True
    return False

print(more_than_n([2, 4, 6, 2, 3, 2, 1, 2], 2, 3))

# ------------------------------#

# 4: Append Size
def append_size(lst):
    # append the size of the list to the end of the list and return the new list
    size = len(lst)
    lst.append(size)

    # return the list
    return lst

print(append_size([23, 42, 108]))

# ------------------------------#

# 5: Combine Sort
def combine_sort(list1, list2):
    # combine the two lists
    both_lists = list1 + list2

    # sort the new list
    both_lists.sort()

    # return the new list
    return both_lists

print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]))
