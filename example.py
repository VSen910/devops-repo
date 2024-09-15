
#Contributer Vineet Sen
def add(a, b):
    return a+b

#Contributer Nischay Kondai
def modu(x, y):
    return x%y

#Contributer Pratik Raj
def sub(a, b):
    return a-b

#Contributer Sai Kartik Hosur
def insertionSort(arr):
    n = len(arr)  # Get the length of the array
      
    if n <= 1:
        return  # If the array has 0 or 1 element, it is already sorted, so return
 
    for i in range(1, n):  # Iterate over the array starting from the second element
        key = arr[i]  # Store the current element as the key to be inserted in the right position
        j = i-1
        while j >= 0 and key < arr[j]:  # Move elements greater than key one position ahead
            arr[j+1] = arr[j]  # Shift elements to the right
            j -= 1
        arr[j+1] = key  # Insert the key in the correct position
  
# Sorting the array [12, 11, 13, 5, 6] using insertionSort
arr = [12, 11, 13, 5, 6]
insertionSort(arr)
print(arr)

def bubble_sort(arr):

    # Outer loop to iterate through the list n times
    for n in range(len(arr) - 1, 0, -1):

        # Inner loop to compare adjacent elements
        for i in range(n):
            if arr[i] > arr[i + 1]:

                # Swap elements if they are in the wrong order
                swapped = True
                arr[i], arr[i + 1] = arr[i + 1], arr[i]


# Sample list to be sorted
arr = [39, 12, 18, 85, 72, 10, 2, 18]
print("Unsorted list is:")
print(arr)

bubble_sort(arr)

print("Sorted list is:")
print(arr)

#Hanson George's Contribution 

num_list = [12, 36, 48, 55, 23, 45, 67, 89, 36]
count = 0
for index, num in enumerate(num_list):
    count += 1
    if num > 45:
        print("Over 45")
    else:
        print("Under 45")
    if num == 36:
        print('Number found at position:', index)
        break
print("Total iterations before break:", count)


#Guntreddy Hemanth Contribution 

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

factorial(5)
