def linear_search(arr, target):
    for item in arr:  # Visits each element once
        if item == target:
            return True
    return False