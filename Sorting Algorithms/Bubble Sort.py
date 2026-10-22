numbers = [64, 34, 25, 12, 22, 11, 90]
swaps = 0

def bubble_sort(arr, swaps):
    length = len(arr)
    for i in range(length):
        for j in range(0, length-i-1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
                swaps +=1

    return swaps
                
print("Original array:", numbers)
swaps = bubble_sort(numbers, swaps)
print("Sorted array:", numbers)
print("Number of swaps:", swaps)