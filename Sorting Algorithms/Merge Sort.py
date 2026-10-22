numbers = [64, 34, 25, 12, 22, 11, 90]

def Split(arr):
    splitArray = [[], []]
    for i in range(len(arr)):
        if(i < len(arr)/2):
            splitArray[0].append(arr[i])
        else:
            splitArray[1].append(arr[i])
    return splitArray

def merge(left, right):
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

def sort(arr):
    if len(arr) <= 1:
        return arr
    splitArray = Split(arr)
    left = sort(splitArray[0])
    right = sort(splitArray[1])
    return merge(left, right) 

print("Original array:", numbers)
sorted_array = sort(numbers)
print("Sorted array:", sorted_array)