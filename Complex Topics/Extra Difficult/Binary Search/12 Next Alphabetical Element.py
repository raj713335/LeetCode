def next_alphabetical_element(letters, target):
    low, high = 0, len(letters) - 1
    result = letters[0]  # Wrap around case

    while low <= high:
        mid = (low + high) // 2

        if letters[mid] > target:
            result = letters[mid]
            high = mid - 1
        else:
            low = mid + 1

    return result

# Example usage:
letters = ['a', 'c', 'f', 'h']
target = 'f'
print(f"Next letter after '{target}' is '{next_alphabetical_element(letters, target)}'")
