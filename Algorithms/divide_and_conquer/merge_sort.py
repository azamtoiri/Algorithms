# MERGE SORT
import time
from random import randint


def sort_array(arr: list) -> list:  # Works for arrays: 1 <= nums.length <= 5 * 104; -5 * 104 <= nums[i] <= 5 * 104
    if len(arr) <= 1:
        return arr
    middle = len(arr) // 2
    left = sort_array(arr[middle:])
    right = sort_array(arr[:middle])
    merged = []
    while left and right:
        if left[0] <= right[0]:
            merged.append(left.pop(0))
        else:
            merged.append(right.pop(0))
    merged.extend(right if right else left)
    return merged


def merge_sort(left: list, right: list) -> list:  # NOT WORKS!
    ans = []
    while min(len(left), len(right)) > 0:
        if left[0] > right[0]:
            insert = right.pop(0)
            ans.append(insert)
        elif left[0] <= right[0]:
            insert = left.pop(0)
            ans.append(insert)
    if len(left) > 0:
        for i in left:
            ans.append(i)
    if len(right) > 0:
        for i in right:
            ans.append(i)
    return ans


def brut_force_method(arr: list) -> list:
    ans = []
    while arr:
        minimum = arr[0]
        for x in arr:
            if x < minimum:
                minimum = x
        ans.append(minimum)
        arr.remove(minimum)
    return ans


def insert_sort(arr: list):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def gen_list() -> list:  # generate array size 1000 with random values from 1 to 1003
    arr = []
    for i in range(1000):
        rand = randint(1, 1003)
        arr.append(rand)
    return arr


gen = gen_list()

A = [-5, -23, 5, 0, 23, -6, 23, 67]
# print(brut_force_method(gen))     # 0.018002748489379883
# print(insert_sort(gen))           # 0.05200052261352539
# print(merge_sort(gen, A))         # 0.0010328292846679688
start = time.time()
print(sort_array(gen))  # 0.005081653594970703
end = time.time()
print(end - start)
sorted()
