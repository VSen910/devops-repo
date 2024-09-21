# Contributor Devapangu Abhishek
def bucket_insertion_sort(bucket):
    for i in range(1, len(bucket)):
        key = bucket[i]
        j = i - 1
        while j >= 0 and bucket[j] > key:
            bucket[j + 1] = bucket[j]
            j -= 1
        bucket[j + 1] = key


def bucket_sort(arr):
    n = len(arr)
    buckets = [[] for _ in range(n)]

    # Put array elements in different buckets
    for num in arr:
        bi = int(n * num)
        buckets[bi].append(num)

    # Sort individual buckets using insertion sort
    for bucket in buckets:
        bucket_insertion_sort(bucket)

    # Concatenate all buckets into arr[]
    index = 0
    for bucket in buckets:
        for num in bucket:
            arr[index] = num
            index += 1


# Contributor Vineet Sen
def merge(arr, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid

    L = [0] * n1
    R = [0] * n2

    # Separate out the two halves
    for i in range(n1):
        L[i] = arr[left + i]
    for j in range(n2):
        R[j] = arr[mid + 1 + j]

    i = 0
    j = 0
    k = left

    # Merge the halves while sorting
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


def merge_sort(arr, left, right):
    if left < right:
        mid = (left + right) // 2

        # Divide the array into halves
        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)

        # Sort and merge the halves
        merge(arr, left, mid, right)


# Contributer Nischay Kondai

# Selection sort in Python
# time complexity O(n*n)
# sorting by finding min_index
def selection_sort(array):
    size = len(array)
    for ind in range(size):
        min_index = ind

        for j in range(ind + 1, size):
            # select the minimum element in every iteration
            if array[j] < array[min_index]:
                min_index = j
        # swapping the elements to sort the array
        (array[ind], array[min_index]) = (array[min_index], array[ind])


# Contributer Pratik Raj
def partition(array, low, high):
    pivot = array[high]
    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])

    (array[i + 1], array[high]) = (array[high], array[i + 1])
    return i + 1


def quick_sort(array, low, high):
    if low < high:
        pi = partition(array, low, high)

        quick_sort(array, low, pi - 1)

        quick_sort(array, pi + 1, high)


# Contributer Sai Kartik Hosur
def insertion_sort(arr):
    n = len(arr)  # Get the length of the array

    if n <= 1:
        return  # If the array has 0 or 1 element, it is already sorted, so return

    for i in range(1, n):  # Iterate over the array starting from the second element
        key = arr[i]  # Store the current element as the key to be inserted in the right position
        j = i - 1
        while j >= 0 and key < arr[j]:  # Move elements greater than key one position ahead
            arr[j + 1] = arr[j]  # Shift elements to the right
            j -= 1
        arr[j + 1] = key  # Insert the key in the correct position


# Contributor Abhishikth Guddanti
def bubble_sort(arr):
    # Outer loop to iterate through the list n times
    for n in range(len(arr) - 1, 0, -1):

        # Inner loop to compare adjacent elements
        for i in range(n):
            if arr[i] > arr[i + 1]:
                # Swap elements if they are in the wrong order
                swapped = True
                arr[i], arr[i + 1] = arr[i + 1], arr[i]


# Contributor Guntreddy Hemanth
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result


# Contributor RK
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        # Check if target is present at mid
        if arr[mid] == target:
            return mid
        # If target is greater, ignore the left half
        elif arr[mid] < target:
            low = mid + 1
        # If target is smaller, ignore the right half
        else:
            high = mid - 1
    # Target is not present in array
    return -1


# Contributer Hanson George
def linear_search(arr, target):
    for i in range(len(arr)):

        if arr[i] == target:
            return i
    return -1


choice_string = '''
Choose a number:
1. Bubble sort
2. Selection sort
3. Insertion sort
4. Merge sort
5. Quick sort
6. Bucket sort
7. Linear search
8. Binary search
9. Factorial
'''
choice = int(input(f'{choice_string}\n'))

if choice == 1:
    arr = []
    n = int(input('No. of elements: \n'))
    for i in range(0, n):
        arr.append(int(input()))

    print("Unsorted list is:")
    print(arr)

    bubble_sort(arr)

    print("Sorted list is:")
    print(arr)
elif choice == 2:
    arr = []
    n = int(input('No. of elements: \n'))
    for i in range(0, n):
        arr.append(int(input()))

    print("Unsorted list is:")
    print(arr)

    selection_sort(arr)

    print("Sorted list is:")
    print(arr)
elif choice == 3:
    arr = []
    n = int(input('No. of elements: \n'))
    for i in range(0, n):
        arr.append(int(input()))

    print("Unsorted list is:")
    print(arr)

    insertion_sort(arr)

    print("Sorted list is:")
    print(arr)
elif choice == 4:
    arr = []
    n = int(input('No. of elements: \n'))
    for i in range(0, n):
        arr.append(int(input()))

    print("Unsorted list is:")
    print(arr)

    merge_sort(arr, 0, len(arr) - 1)

    print("Sorted list is:")
    print(arr)
elif choice == 5:
    arr = []
    n = int(input('No. of elements: \n'))
    for i in range(0, n):
        arr.append(int(input()))

    print("Unsorted list is:")
    print(arr)

    quick_sort(arr, 0, len(arr) - 1)

    print("Sorted list is:")
    print(arr)
elif choice == 6:
    arr = []
    n = int(input('No. of elements: \n'))
    for i in range(0, n):
        arr.append(float(input()))

    print("Unsorted list is:")
    print(arr)

    bucket_sort(arr)

    print("Sorted list is:")
    print(arr)
elif choice == 7:
    arr = []
    n = int(input('No. of elements: \n'))
    for i in range(0, n):
        arr.append(int(input()))
    target = int(input('Enter target: \n'))

    res = linear_search(arr, target)

    if res != -1:
        print(f'Element found at: {res}')
    else:
        print('Element not found')
elif choice == 8:
    arr = []
    n = int(input('No. of elements: \n'))
    for i in range(0, n):
        arr.append(int(input()))
    target = int(input('Enter target: \n'))

    res = binary_search(arr, target)

    if res != -1:
        print(f'Element found at: {res}')
    else:
        print('Element not found')
elif choice == 9:
    n = int(input('Enter a number: \n'))
    print(f'Factorial of {n}: {factorial(n)}')
