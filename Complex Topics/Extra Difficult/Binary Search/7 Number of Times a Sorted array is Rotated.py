def count_rotations(arr):
    low, high = 0, len(arr) - 1
    
    while low <= high:
        # Case when subarray is already sorted
        if arr[low] <= arr[high]:
            return low

        mid = (low + high) // 2
        next_ = (mid + 1) % len(arr)
        prev_ = (mid - 1 + len(arr)) % len(arr)

        # Check if mid is the minimum
        if arr[mid] <= arr[next_] and arr[mid] <= arr[prev_]:
            return mid
        
        # Decide which half to choose
        if arr[mid] >= arr[low]:
            low = mid + 1
        else:
            high = mid - 1

    return 0  # fallback
