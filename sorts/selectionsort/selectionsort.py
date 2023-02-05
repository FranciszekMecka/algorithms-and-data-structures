arr = [ 23, 27, 12, 79, 80, 21, 54, 24, 1, 58, 92, 55, 54, 49, 42, 59, 99, 54, 58, 9, 87, 9, 53, 12, 82, 45, 69, 66, 82, 8, 67, 21, 25, 3, 18, 42, 42, 11, 61, 61, 70, 40, 49, 37, 82, 83, 22, 87, 18, 65, 48, 33, 54, 25, 71, 14, 3, 80, 57, 50, 48, 1, 21, 38, 86, 63, 37, 43, 78, 62, 67, 40, 88, 35, 1, 96, 24, 73, 64, 86, 21, 83, 83, 57, 41, 16, 81, 38, 88, 65, 44, 60, 63, 7, 47, 53, 58, 98, 56, 78]

def selection_sort(arr):
    for i in range (len(arr)):
        min = arr[i]
        min_index = i
        for n in range (i, len(arr)):
            if min > arr[n]:
                min = arr[n]
                min_index = n
        arr[i], arr[min_index] = arr[min_index], arr[i]
                
selection_sort(arr)

print(arr)