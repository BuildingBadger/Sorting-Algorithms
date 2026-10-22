import threading
import time

numbers = [4, 3, 2, 1, 5]

def sleep_sort(arr):
    threads = []
    sorted_arr = []

    def sleepAndAppend(num):
        time.sleep(num)
        sorted_arr.append(num)

    for num in arr:
        thread = threading.Thread(target=sleepAndAppend, args=(num,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return sorted_arr

print("Original array:", numbers)
sorted_array = sleep_sort(numbers)
print("Sorted array:", sorted_array)