# INSERTION SORT

def insert_sort(arr: list):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def insert_sort2(arr: list):  # INSERT SORT for 2 dimensional arrays
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            key = arr[i][j]
            k = j - 1
            while k >= 0 and arr[i][k] > key:
                arr[i][k + 1] = arr[i][k]
                k -= 1
            arr[i][k + 1] = key
    return arr


A = [8, 234, 231, 43, 54, 32, 2, 3, 0]
A2 = [
    [2, 0, 1, 4],
    [1, 21, 2],
    [10, 2, 1],
]

print(insert_sort(A))
print(insert_sort2(A2))
