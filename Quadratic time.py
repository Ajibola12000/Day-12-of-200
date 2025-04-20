def bubble_sort(arr):
    n = len(arr)
    for i in range(n):          # Outer loop: n iterations
        for j in range(n-i-1):  # Inner loop: n-i-1 iterations
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]