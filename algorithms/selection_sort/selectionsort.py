import time

__author__ = 'jay'


def selection_sort(some_list: list, desc: bool = False):
    """
    Sorts a given list using Selection Sort algorithm

    :param some_list: List to be sorted
    :param desc: List is sorted descending if True, else in ascending in order
    :return: None
    """
    total_iter = 0
    for idx in range(0, len(some_list) - 1):
        current_min = some_list[idx]
        current_idx = idx
        swap_idx = idx
        for num in some_list[idx:]:
            condition = (num > current_min) if desc else (num < current_min)
            if condition:
                current_min = num
                swap_idx = current_idx
            current_idx += 1
            total_iter += 1
        temp = some_list[idx]
        some_list[idx] = current_min
        some_list[swap_idx] = temp

    print("total iteration: %d" % total_iter)


numbers = [2, 3, 1, 2, 3, 1, 56, 23, 1, 232, 11, 232, 100, 2, 3, 1, 2, 3, 1, 56, 23, 1, 232, 11, 232, 100]

start_time = time.clock()
selection_sort(numbers)
print(numbers)
print("Time taken %f sec" % (time.clock() - start_time))
