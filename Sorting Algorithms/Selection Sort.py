numbers = [64, 34, 25, 12, 22, 11, 90]
swaps = 0

def selection_sort(arr, swaps):
    length = len(arr)
    for i in range(length):
        min_idx = i
        for j in range(i+1, length):
            if arr[j] < arr[min_idx]:
                min_idx = j
        if min_idx != i:
            temp = arr[i]
            arr[i] = arr[min_idx]
            arr[min_idx] = temp
            swaps += 1
    return swaps

print("Original array:", numbers)
swaps = selection_sort(numbers, swaps)
print("Sorted array:", numbers)
print("Number of swaps:", swaps)