numbers = [64, 34, 25, 12, 22, 11, 90]

def Shaker_Sort(arr):
    n = len(arr)
    swapped = True
    start = 0
    end = n - 1

    while swapped:
        swapped = False

        for i in range(start, end):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True

        if not swapped:
            break

        swapped = False
        end -= 1

        for i in range(end, start - 1, -1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True

        start += 1

    return arr

print("Original array:", numbers)
sorted_array = Shaker_Sort(numbers)
print("Sorted array:", sorted_array)