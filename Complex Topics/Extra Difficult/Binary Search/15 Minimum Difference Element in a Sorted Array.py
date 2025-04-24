def find_min_diff_element(arr, x):
    low, high = 0, len(arr) - 1

    # Handle edge cases
    if x <= arr[0]:
        return arr[0]
    if x >= arr[-1]:
        return arr[-1]

    # Binary search
    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == x:
            return arr[mid]
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1

    # Now arr[high] < x < arr[low]
    if abs(arr[low] - x) < abs(arr[high] - x):
        return arr[low]
    else:
        return arr[high]

# Example usage
arr = [1, 3, 8, 10, 15]
x = 12
print(f"Element with minimum difference to {x} is {find_min_diff_element(arr, x)}")
