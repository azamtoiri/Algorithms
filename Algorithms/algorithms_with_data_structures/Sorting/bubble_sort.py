# BUBBLE SORT - OPTIMIZED VS UNOPTIMIZED

def bubble_sort(arr: list) -> tuple:
    iterations = 0
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            iterations += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr, iterations


def bubble_sort2(arr: list) -> tuple:  # better
    iterations = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr) - 1):
            iterations += 1
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr, iterations


# region: UNOPTIMIZED
def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


def bubble_sort_un_op(arr: list) -> tuple:
    iterations = 0
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            iterations += 1
            if arr[j] > arr[j + 1]:
                swap(arr, j, j + 1)
    return arr, iterations

# endregion


A = [8, 234, 231, 43, 54, 32, 2, 3, 0]
print(bubble_sort(arr=A))  # 36 iterations
print(bubble_sort2(arr=A))  # 28 iterations
print(bubble_sort_un_op(arr=A))
