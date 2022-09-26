# Search and sort

# return index position of searching element
def simple_search(arr: list, target: int) -> int:
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


arr = [2, 3, 5, 6, 7]
target = 6
print(simple_search(arr, target))
