import random

numbers = [64, 34, 25, 12, 22, 11, 90]
shuffles = 0

def CheckSorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True

def BogoSort(arr, shuffles):
    while not CheckSorted(arr):
        random.shuffle(arr)
        shuffles += 1
    return shuffles

print("Original array:", numbers)
shuffles = BogoSort(numbers, shuffles)
print("Sorted array:", numbers)
print("Number of shuffles:", shuffles)
