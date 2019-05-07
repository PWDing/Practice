import time
import random

import sort


def find_kth_smallest_item_by_merge_sort(array, k):
    new_array = sort.merge_sort(array)
    return new_array[k-1]


def find_kth_smallest_item(array, k):
    if len(array) < k:
        return None

    maximum = 0
    for num in array:
        if num > maximum:
            maximum = num

    new_array = [0 for i in range(maximum+1)]
    for j in range(len(array)):
        new_array[array[j]] += 1

    count = 0
    for n in range(maximum+1):
        while new_array[n] > 0:
            count += 1
            if count == k:
                return n
            new_array[n] -= 1
    return None


test_list = list(range(1, 100000))
random.shuffle(test_list)
backup = test_list[:]
start = time.time()
result1 = find_kth_smallest_item_by_merge_sort(backup, 8888)
end = time.time()
print(result1)
print("time cost: ", end-start)
print("*" * 36)

backup = test_list[:]
start = time.time()
result2 = find_kth_smallest_item(backup, 8888)
end = time.time()
print(result2)
print("time cost: ", end-start)
print("*" * 36)
