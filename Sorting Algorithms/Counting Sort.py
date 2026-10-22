numbers = [64, 34, 25, 12, 22, 11, 90]
k = 100

def counting_sort(arr, k):
    count = [0] * (k + 1)
    output = [0] * len(arr)

    for num in arr:
        count[num] += 1

    for i in range(1, len(count)):
        count[i] += count[i - 1]

    for num in reversed(arr):
        output[count[num] - 1] = num
        count[num] -= 1

    return output

print("Original array:", numbers)
sorted_array = counting_sort(numbers, k)
print("Sorted array:", sorted_array)
        