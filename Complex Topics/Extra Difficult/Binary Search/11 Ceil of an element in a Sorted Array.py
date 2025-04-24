def find_ceil(arr, x):
    low, high = 0, len(arr) - 1
    ceil_index = -1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == x:
            return mid  # Exact match is the ceil
        elif arr[mid] < x:
            low = mid + 1
        else:
            ceil_index = mid  # Potential ceil
            high = mid - 1

    return ceil_index

# Example usage:
arr = [1, 2, 8, 10, 10, 12, 19]
x = 5
index = find_ceil(arr, x)

if index != -1:
    print(f"Ceil of {x} is {arr[index]} at index {index}")
else:
    print(f"No ceil found for {x}")
