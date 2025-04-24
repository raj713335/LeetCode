def find_floor(arr, x):
    low, high = 0, len(arr) - 1
    floor_index = -1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == x:
            return mid  # Exact match is the floor
        elif arr[mid] < x:
            floor_index = mid  # Potential floor
            low = mid + 1
        else:
            high = mid - 1

    return floor_index

# Example usage:
arr = [1, 2, 8, 10, 10, 12, 19]
x = 5
index = find_floor(arr, x)

if index != -1:
    print(f"Floor of {x} is {arr[index]} at index {index}")
else:
    print(f"No floor found for {x}")
