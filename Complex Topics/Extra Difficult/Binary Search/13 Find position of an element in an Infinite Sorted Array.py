def binary_search(arr, target, low, high):
    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def find_position_in_infinite_array(arr, target):
    # Start with a small range
    low, high = 0, 1

    # Expand range until target is less than high index value
    while high < len(arr) and arr[high] < target:
        low = high
        high = high * 2
        if high >= len(arr):  # Ensure we don't go out of bounds
            high = len(arr) - 1

    # Apply binary search in the found range
    return binary_search(arr, target, low, high)

# Simulate an "infinite" sorted array
arr = [3, 5, 7, 9, 10, 13, 15, 18, 20, 24, 27, 30, 34, 38, 41, 45, 49]
target = 34
index = find_position_in_infinite_array(arr, target)

if index != -1:
    print(f"Element {target} found at index {index}")
else:
    print(f"Element {target} not found")
