def find_first_one(arr):
    # Step 1: Find range for binary search
    low, high = 0, 1

    while high < len(arr) and arr[high] == 0:
        low = high
        high *= 2
        if high >= len(arr):
            high = len(arr) - 1
            break

    # Step 2: Binary search for first 1
    result = -1
    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == 1:
            result = mid
            high = mid - 1  # Search on left side for earlier 1
        else:
            low = mid + 1

    return result

# Example usage:
arr = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1]
print("First 1 at index:", find_first_one(arr))
