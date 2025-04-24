# A bitonic array is a special type of array that:
## Strictly increases up to a certain point (called the peak), and then
## Strictly decreases after that point.

def find_max_in_bitonic_array(arr):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        left = arr[mid - 1] if mid > 0 else float('-inf')
        right = arr[mid + 1] if mid < len(arr) - 1 else float('-inf')

        if arr[mid] > left and arr[mid] > right:
            return arr[mid]  # Peak element
        elif arr[mid] < right:
            low = mid + 1  # Go right (increasing part)
        else:
            high = mid - 1  # Go left (decreasing part)

# Example usage:
arr = [1, 3, 8, 12, 4, 2]
print(f"Maximum in Bitonic Array: {find_max_in_bitonic_array(arr)}")


