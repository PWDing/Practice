import time
import random


def check_list(array):
    if array is None:
        array = []
    return array


def bubble_sort(array=None):
    check_list(array)
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if array[j] < array[i]:
                array[i], array[j] = array[j], array[i]
    return array


def selection_sort(array=None):
    check_list(array)
    for i in range(len(array)):
        min_number = array[i]
        for j in range(i+1, len(array)):
            if array[j] < min_number:
                min_number, array[j] = array[j], min_number
        array[i] = min_number
    return array


def insert_sort(array=None):
    check_list(array)
    for i in range(1, len(array)):
        mark = array[i]
        for j in range(i-1, -1, -1):
            if array[j] <= mark:
                array[j+1] = mark
                break
            array[j+1] = array[j]
    return array


def merge_sort(array=None):
    check_list(array)
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    left_half = array[:mid]
    right_half = array[mid:]

    merge_sort(left_half)
    merge_sort(right_half)

    left_index = 0
    right_index = 0
    merge_index = 0

    while left_index < len(left_half) and right_index < len(right_half):
        if left_half[left_index] < right_half[right_index]:
            array[merge_index] = left_half[left_index]
            left_index += 1
        else:
            array[merge_index] = right_half[right_index]
            right_index += 1
        merge_index += 1
    while left_index < len(left_half):
        array[merge_index] = left_half[left_index]
        left_index += 1
        merge_index += 1
    while right_index < len(right_half):
        array[merge_index] = right_half[right_index]
        right_index += 1
        merge_index += 1
    return array


def quick_sort(start, end, array=None):
    check_list(array)
    if len(array) <= 1:
        return array

    if start < end:
        pivot = partition(start, end, array)
        quick_sort(start, pivot-1, array)
        quick_sort(pivot+1, end, array)
    return array


def partition(start, end, array=None):
    pivot = start - 1
    reference = array[end]
    for i in range(start, end):
        if array[i] <= reference:
            pivot += 1
            array[pivot], array[i] = array[i], array[pivot]
    pivot += 1
    array[pivot], array[end] = array[end], array[pivot]
    return pivot


def heapify(list_, root, size):
    check_list(list_)

    largest = root
    left_child = root * 2 + 1
    right_child = root * 2 + 2

    if left_child < size and list_[left_child] > list_[largest]:
        largest = left_child
    if right_child < size and list_[right_child] > list_[largest]:
        largest = right_child
    if root != largest:
        list_[root], list_[largest] = list_[largest], list_[root]
        heapify(list_, largest, size)


def heap_sort(list_, root, size):
    check_list(list_)

    # build max-heap
    sub_node = size // 2 - 1
    while sub_node >= 0:
        heapify(list_, sub_node, size)
        sub_node -= 1

    for i in range(size-1, 0, -1):
        list_[root], list_[i] = list_[i], list_[root]
        heapify(list_, root, i)


def find_kth_smallest_num(array, k):
    if len(array) < k:
        return None
    return merge_sort(array)[k-1]


def display_sort_time(sort_name, unsort_list):
    if sort_name == 'bubble':
        start_time = time.time()
        bubble_sort(unsort_list)
        end_time = time.time()
    elif sort_name == 'select':
        start_time = time.time()
        selection_sort(unsort_list)
        end_time = time.time()
    elif sort_name == 'insert':
        start_time = time.time()
        insert_sort(unsort_list)
        end_time = time.time()
    elif sort_name == 'merge':
        start_time = time.time()
        merge_sort(unsort_list)
        end_time = time.time()
    elif sort_name == 'quick':
        start_time = time.time()
        quick_sort(0, len(unsort_list)-1, unsort_list)
        end_time = time.time()
    elif sort_name == 'heap':
        start_time = time.time()
        heap_sort(unsort_list)
        end_time = time.time()
    elif sort_name == 'find':
        start_time = time.time()
        result = find_kth_smallest_num(unsort_list, 12)
        print(result)
        end_time = time.time()

    print("Sort Method".center(36))
    print("{} sort's cost is {}".format(sort_name, (end_time-start_time)))
    print("*" * 52)


test_list = list(range(1, 10000))
random.shuffle(test_list)
# while True:
#     backup = test_list[:]
#     sort_method_name = input("Please enter sort method name: ")
#
#     display_sort_time(sort_method_name, backup)
