arr = [ 5, 3, 10, 2, 4, 80, 21, 54, 24, 1, 58, 92, 55, 54, 49, 42, 59, 99, 813, 54, 58, 9, 87, 9, 53, 12, 82, 45, 69, 66, 82, 8, 67, 21, 25, 3, 18, 42, 42, 11, 61, 61, 70, 40, 49, 37, 82, 83, 22, 87, 18, 65, 48, 33, 54, 25, 71, 14, 3, 80, 57, 50, 48, 1, 21, 38, 86, 63, 37, 43, 78, 62, 67, 40, 88, 35, 1, 96, 24, 73, 64, 86, 21, 83, 83, 57, 41, 16, 81, 38, 88, 65, 44, 60, 63, 7, 47, 53, 58, 98, 56, 78]

def partition(arr, l, r):
    pivot = arr[l]
    l_p = l - 1
    r_p = r + 1
    while True:
        while True:
            l_p = l_p + 1
            if arr[l_p] >= pivot : break
        while True:
            r_p = r_p - 1
            if arr[r_p] <= pivot : break
        if (l_p < r_p):
            arr[l_p], arr[r_p] = arr[r_p], arr[l_p]
        else:
            return r_p

def quick_sort(arr, l, r):
    if (l < r):
        q = partition(arr, l, r)
        quick_sort (arr, l, q)
        quick_sort (arr, q+1, r)

quick_sort(arr, 0, len(arr) - 1)

print(arr)
def check_if_sorted(arr):
    for n in range(len(arr) - 1):
        if arr[n] > arr[n + 1]:
            return False
    return True
print(check_if_sorted(arr))
