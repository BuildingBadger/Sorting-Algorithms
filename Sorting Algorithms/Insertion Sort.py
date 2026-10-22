numbers = [64, 34, 25, 12, 22, 11, 90]
insertions = 0

def insertion_sort(arr, insertions):
    length = len(arr)
    for i in range(1, length):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
            insertions += 1
        arr[j + 1] = key
    return insertions

print("Original array:", numbers)
insertions = insertion_sort(numbers, insertions)
print("Sorted array:", numbers)
print("Number of insertions:", insertions)