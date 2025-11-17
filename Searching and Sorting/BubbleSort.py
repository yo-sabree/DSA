def bubble(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j] 

    return arr

def buggle(arr):
    n = len(arr)
    for i in range(0,n-1):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i] 
    n = n-1
    return arr


arr = [64, 34, 25, 12, 22, 11, 90]
print("Unsorted array:", arr)
sorted_arr = bubble(arr)
print("Sorted array:", sorted_arr)  