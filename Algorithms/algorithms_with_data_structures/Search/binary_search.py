# Binary search

# return index position of searching element
def bin_search(arr: list, target: int) -> int:  # uses only with sorted array
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


# recursive binary search
def binary_recur(arr: list, start: int, end: int, target: int) -> int:  # use only with sorted array
    if end >= start:
        mid = start + end - 1 // 2

        if arr[mid] < target:
            binary_recur(arr, mid + 1, end, target)
        elif arr[mid] > target:
            return binary_recur(arr, start, mid - 1, target)
        else:
            return mid
    else:
        return -1


arr = [10, 33, 34, 52, 62]
target = 10
print(bin_search(arr, target))
print(binary_recur(arr, 0, len(arr) - 1, target))
