import time
import random

import sort


def linear_search(alist, goal):
    if alist is None:
        return False
    size = len(alist)
    for i in range(size):
        if alist[i] == goal:
            return i
    return False


def binary_search(ordered_list, goal):
    if ordered_list is None:
        return False

    first = 0
    last = len(ordered_list) - 1
    while first <= last:
        mid = (first+last) // 2
        if ordered_list[mid] == goal:
            return mid
        else:
            if ordered_list[mid] > goal:
                last = mid - 1
            else:
                first = mid + 1
    return False


def find_kth_smallest_num(alist, k):
    if len(alist) < k:
        return None

    # find the largest number
    maximum = 0
    for num in alist:
        if num > maximum:
            maximum = num

    # generate an array of size maximum
    max_size_array = [0] * (maximum + 1)
    # record pending numbers and count their occurrence
    for num in alist:
        max_size_array[num] += 1

    counter = 0
    for i in range(maximum+1):
        while max_size_array[i]:
            counter += 1
            if counter == k:
                return i
            max_size_array[i] -= 1


def test_perfermence(method, alist, goal):
    if method == 'linear':
        start = time.time()
        result = linear_search(alist, goal)
        end = time.time()
    elif method == 'binary':
        sort.merge_sort(alist)
        start = time.time()
        result = binary_search(alist, goal)
        end = time.time()
    elif method == 'find_kth':
        start = time.time()
        result = find_kth_smallest_num(alist, goal)
        end = time.time()
    else:
        start = 0
        end = 0
        result = None

    print("The target is:", goal)
    print("The result of {} search is {}.".format(method, result))
    print("It costs {}.".format(end-start))
    print("*" * 52)


if __name__ == '__main__':
    test_list = list(range(100000))
    random.shuffle(test_list)
    while True:
        search_method_name = input("Please enter the method: ")
        mylist = test_list[:]
        target = random.randrange(0, 100000)
        test_perfermence(search_method_name, mylist, target)
