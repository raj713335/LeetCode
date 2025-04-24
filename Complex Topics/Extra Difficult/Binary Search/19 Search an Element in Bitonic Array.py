# A bitonic array is a special type of array that:
# Strictly increases up to a certain point (called the peak), and then
# Strictly decreases after that point.

def find_peak(arr):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        left = arr[mid - 1] if mid > 0 else float('-inf')
        right = arr[mid + 1] if mid < len(arr) - 1 else float('-inf')

        if arr[mid] > left and arr[mid] > right:
            return mid
        elif arr[mid] < right:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def binary_search(arr, target, low, high, ascending=True):
    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid

        if ascending:
            if arr[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        else:
            if arr[mid] < target:
                high = mid - 1
            else:
                low = mid + 1

    return -1

def search_bitonic_array(arr, target):
    peak = find_peak(arr)

    # Try to find target in increasing part
    index = binary_search(arr, target, 0, peak, ascending=True)
    if index != -1:
        return index

    # Try to find target in decreasing part
    return binary_search(arr, target, peak + 1, len(arr) - 1, ascending=False)

# Example usage:
arr = [1, 3, 8, 12, 9, 5, 2]
target = 9
index = search_bitonic_array(arr, target)
if index != -1:
    print(f"Element {target} found at index {index}")
else:
    print(f"Element {target} not found")
