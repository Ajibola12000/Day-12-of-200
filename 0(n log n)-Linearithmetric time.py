def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])  # O(log n) splits
    right = merge_sort(arr[mid:])
    return merge(left, right)     # O(n) merge per split