import random

numbers = [64, 34, 25, 12, 22, 11, 90]
k = max(numbers)

def counting_sort(arr, exp):
    count = [0] * 10
    output = [0] * len(arr)

    for num in arr:
        index = (num // exp) % 10
        count[index] += 1

    for i in range(1, len(count)):
        count[i] += count[i - 1]

    for num in reversed(arr):
        index = (num // exp) % 10
        output[count[index] - 1] = num
        count[index] -= 1

    return output

def Radix_sort(arr, k):
    exp = 1
    while k // exp > 0:
        arr = counting_sort(arr, exp)
        exp *= 10
    return arr

print("Original array:", numbers)
sorted_array = Radix_sort(numbers, k)
print("Sorted array:", sorted_array)