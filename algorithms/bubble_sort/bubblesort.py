import time

__author__ = 'jay'


def bubble_sort(some_list: list):
    """
    Sorts the provided list using bubble sort algorithm

    Parameters
    -----------
    some_list: list
        List which will be sorted
    """
    total_sorted = 0
    idx = list_len = len(some_list)
    while total_sorted < list_len - 1:
        while idx >= 2 + total_sorted:
            num2 = some_list[idx - 1]
            num1 = some_list[idx - 2]
            if num2 < num1:
                some_list[idx - 1] = num1
                some_list[idx - 2] = num2
            idx -= 1

        total_sorted += 1
        idx = list_len


my_list = [2, 3, 1, 2, 3, 1, 56, 23, 1, 232, 11, 232, 100, 2, 3, 1, 2, 3, 1, 56, 23, 1, 232, 11, 232, 100]

start_time = time.clock()
bubble_sort(my_list)
print(my_list)
print("Time taken %f sec" % (time.clock() - start_time))
