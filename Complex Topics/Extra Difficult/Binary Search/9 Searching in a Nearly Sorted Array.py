def search_nearly_sorted(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        # Check mid
        if arr[mid] == target:
            return mid
        # Check mid - 1
        if mid - 1 >= low and arr[mid - 1] == target:
            return mid - 1
        # Check mid + 1
        if mid + 1 <= high and arr[mid + 1] == target:
            return mid + 1

        # If target is smaller, ignore right part
        if target < arr[mid]:
            high = mid - 2
        # If target is greater, ignore left part
        else:
            low = mid + 2

    return -1  # Target not found

# Example usage
arr = [10, 3, 40, 20, 50, 80, 70]
target = 40
index = search_nearly_sorted(arr, target)
print(f"Element found at index: {index}" if index != -1 else "Element not found")
