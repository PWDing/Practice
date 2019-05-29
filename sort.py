import time
import random


def bubble_sort(alist):
    size = len(alist)
    for i in range(size-1):
        for j in range(size-1, i, -1):
            if alist[j-1] > alist[j]:
                alist[j-1], alist[j] = alist[j], alist[j-1]


def short_bubble(alist):
    index = 0
    size = len(alist)
    is_sorted = False
    while index < size-1 and not is_sorted:
        # 假设已经排好序了，则所有项都不需要交换，下一轮直接退出循环即可
        is_sorted = True

        # 验证假设
        index += 1
        for j in range(size-1, index, -1):
            if alist[j-1] > alist[j]:
                # 发生交换，说明假设错误，将标志变量重置为 false
                is_sorted = False
                alist[j-1], alist[j] = alist[j], alist[j-1]


def selection_sort(alist):
    for i in range(len(alist)-1):
        min_index = i
        for j in range(i+1, len(alist)):
            if alist[j] < alist[min_index]:
                min_index = j
        alist[i], alist[min_index] = alist[min_index], alist[i]


def insert_sort(alist):
    for i in range(1, len(alist)):
        current = alist[i]
        for j in range(i-1, -1, -1):
            if alist[j] <= current:
                alist[j+1] = current
                break
            alist[j+1] = alist[j]


def shell_sort(alist):
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


def merge_sort(alist):
    size = len(alist)
    if size > 1:
        mid = size // 2
        left = alist[:mid]
        right = alist[mid:]

        merge_sort(left)
        merge_sort(right)
        merge(alist, left, right)


def merge(alist, left_half, right_half):
    left_index = 0
    right_index = 0
    merge_index = 0
    left_size = len(left_half)
    right_size = len(right_half)

    while left_index < left_size and right_index < right_size:
        if left_half[left_index] < right_half[right_index]:
            alist[merge_index] = left_half[left_index]
            left_index += 1
        else:
            alist[merge_index] = right_half[right_index]
            right_index += 1
        merge_index += 1
    while left_index < left_size:
        alist[merge_index] = left_half[left_index]
        left_index += 1
        merge_index += 1
    while right_index < right_size:
        alist[merge_index] = right_half[right_index]
        right_index += 1
        merge_index += 1


def quick_sort(alist, first, last):
    if first < last:
        # 选择首数作为基准
        pivot = alist[first]
        start = first + 1
        end = last
        while start <= end:
            while start <= end and alist[start] <= pivot:
                start += 1
            while start <= end and alist[end] >= pivot:
                end -= 1
            if start <= end:
                alist[start], alist[end] = alist[end], alist[start]
        alist[first], alist[end] = alist[end], alist[first]

        quick_sort(alist, first, end-1)
        quick_sort(alist, end+1, last)


def heapify(alist, root, size):
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
    # build max-heap
    sub_node = len(alist) // 2 - 1
    while sub_node >= 0:
        heapify(alist, sub_node, len(alist))
        sub_node -= 1

    # move current largest item to the last position
    for i in range(len(alist)-1, 0, -1):
        alist[0], alist[i] = alist[i], alist[0]
        heapify(alist, 0, i)


def display_sort_time(sort_name, unsort_list):
    if sort_name == 'bubble':
        start_time = time.time()
        bubble_sort(unsort_list)
        end_time = time.time()
    elif sort_name == 'short':
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
        quick_sort(unsort_list, 0, len(unsort_list)-1)
        end_time = time.time()
    elif sort_name == 'heap':
        start_time = time.time()
        heap_sort(unsort_list)
        end_time = time.time()
    else:
        start_time = 0
        end_time = 0

    print(unsort_list)
    print("Sort Method".center(36))
    print("{} sort's cost is {}".format(sort_name, end_time-start_time))
    print("*" * 52)


if __name__ == '__main__':
    test_list = list(range(10000))
    random.shuffle(test_list)
    while True:
        mylist = test_list[:]
        sort_method_name = input("Please enter sort method name: ")
        display_sort_time(sort_method_name, mylist)
