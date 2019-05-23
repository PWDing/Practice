import time
import random


def check_list(alist):
    if alist is None:
        alist = []
    return alist


def bubble_sort(alist=None):
    check_list(alist)
    for i in range(len(alist)-2):
        for j in range(i, len(alist)-1):
            if alist[j] > alist[j+1]:
                alist[j], alist[j+1] = alist[j+1], alist[j]


def short_bubble(alist):
    check_list(alist)
    is_sorted = False
    count = 1
    while count < len(alist)-1 and not is_sorted:
        # 假设已经排好序了，则所有项都不需要交换，下一轮直接退出循环即可
        is_sorted = True

        # 验证假设
        count += 1
        for j in range(count):
            if alist[j] > alist[j+1]:
                # 发生交换，说明假设错误，将标志变量重置为 false
                is_sorted = False
                alist[j], alist[j+1] = alist[j+1], alist[j]


def selection_sort(alist=None):
    check_list(alist)
    for i in range(len(alist)-1):
        min_index = i
        for j in range(i+1, len(alist)):
            if alist[j] < alist[min_index]:
                min_index = j
        alist[i], alist[min_index] = alist[min_index], alist[i]


def insert_sort(alist=None):
    check_list(alist)
    for i in range(1, len(alist)):
        mark = alist[i]
        for j in range(i-1, -1, -1):
            if alist[j] <= mark:
                alist[j+1] = mark
                break
            alist[j+1] = alist[j]


def shell_sort(alist=None):
    check_list(alist)
    size = len(alist)
    # parts 表示将列表分成 parts 段
    parts = size
    while parts > 0:
        # 采用2^k-1(1, 3, 7, 15……)作为增量，则插入排序的时间复杂度可以降到 O(n^(3/2))
        parts //= 3
        # 对每一段依次采用插入排序
        for start in range(parts):
            # start+parts 表示每一段的第二个元素的下标
            for i in range(start+parts, size, parts):
                postion = i
                current = alist[i]
                while postion >= parts and alist[postion-parts] > current:
                    alist[postion] = alist[postion-parts]
                    postion = postion - parts
                alist[postion] = current


def merge_sort(alist=None):
    check_list(alist)
    if len(alist) <= 1:
        return alist
    mid = len(alist) // 2
    left_half = alist[:mid]
    right_half = alist[mid:]

    merge_sort(left_half)
    merge_sort(right_half)

    left_index = 0
    right_index = 0
    merge_index = 0

    while left_index < len(left_half) and right_index < len(right_half):
        if left_half[left_index] < right_half[right_index]:
            alist[merge_index] = left_half[left_index]
            left_index += 1
        else:
            alist[merge_index] = right_half[right_index]
            right_index += 1
        merge_index += 1
    while left_index < len(left_half):
        alist[merge_index] = left_half[left_index]
        left_index += 1
        merge_index += 1
    while right_index < len(right_half):
        alist[merge_index] = right_half[right_index]
        right_index += 1
        merge_index += 1


def quick_sort(start, end, alist=None):
    check_list(alist)
    if len(alist) <= 1:
        return alist

    if start < end:
        pivot = partition(start, end, alist)
        quick_sort(start, pivot-1, alist)
        quick_sort(pivot+1, end, alist)


def partition(start, end, alist=None):
    pivot = start - 1
    reference = alist[end]
    for i in range(start, end):
        if alist[i] <= reference:
            pivot += 1
            alist[pivot], alist[i] = alist[i], alist[pivot]
    pivot += 1
    alist[pivot], alist[end] = alist[end], alist[pivot]
    return pivot


def heapify(alist, root, size):
    check_list(alist)

    largest = root
    left_child = root * 2 + 1
    right_child = root * 2 + 2

    if left_child < size and alist[left_child] > alist[largest]:
        largest = left_child
    if right_child < size and alist[right_child] > alist[largest]:
        largest = right_child
    if root != largest:
        alist[root], alist[largest] = alist[largest], alist[root]
        heapify(alist, largest, size)


def heap_sort(alist):
    check_list(alist)

    # build max-heap
    sub_node = len(alist) // 2 - 1
    while sub_node >= 0:
        heapify(alist, sub_node, len(alist))
        sub_node -= 1

    # move current largest item to the last position
    for i in range(len(alist)-1, 0, -1):
        alist[0], alist[i] = alist[i], alist[0]
        heapify(alist, 0, i)


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


def display_sort_time(sort_name, unsort_list):
    if sort_name == 'bubble':
        start_time = time.time()
        bubble_sort(unsort_list)
        end_time = time.time()
    if sort_name == 'short':
        start_time = time.time()
        short_bubble(unsort_list)
        end_time = time.time()
    elif sort_name == 'select':
        start_time = time.time()
        selection_sort(unsort_list)
        end_time = time.time()
    elif sort_name == 'insert':
        start_time = time.time()
        insert_sort(unsort_list)
        end_time = time.time()
    elif sort_name == 'shell':
        start_time = time.time()
        shell_sort(unsort_list)
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
        find_kth_smallest_num(unsort_list, len(unsort_list)//2)
        end_time = time.time()
    else:
        start_time = time.time()
        end_time = time.time()

    print("Sort Method".center(36))
    print("{} sort's cost is {}".format(sort_name, (end_time-start_time)))
    print("*" * 52)


test_list = list(range(1, 10000))
random.shuffle(test_list)
while True:
    backup = test_list[:]
    sort_method_name = input("Please enter sort method name: ")
    display_sort_time(sort_method_name, backup)
