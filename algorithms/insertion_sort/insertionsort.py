__author__ = "jay"


def insertion_sort(some_list: list, desc: bool = False):
    for idx in range(1, len(some_list)):
        for inner_idx in range(idx, -1, -1):
            if inner_idx == 0:
                break
            num_right = some_list[inner_idx]
            num_left = some_list[inner_idx - 1]
            condition = num_right > num_left if desc else num_right < num_left
            if condition:
                some_list[inner_idx] = num_left
                some_list[inner_idx - 1] = num_right
            else:
                break


numbers = [2, 3, 1, 2, 3, 1, 56, 23, 1, 232, 11, 232, 100, 2, 3, 1, 2, 3, 1, 56, 23, 1, 232, 11, 232, 100]

insertion_sort(numbers, False)
print(numbers)
