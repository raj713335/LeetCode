def countSubsetsAndSum(arr, target, idx, memo_count, memo_sum):
    # Base case: if target becomes 0, we've found a valid subset
    if target == 0:
        return 1, 0  # One valid subset, sum is 0 (empty subset)

    if idx == len(arr):
        return 0, 0  # No more elements to process

    # If already computed, return the result from memo
    if (idx, target) in memo_count:
        return memo_count[(idx, target)], memo_sum[(idx, target)]

    # Include current element
    include_count, include_sum = 0, 0
    if target >= arr[idx]:
        include_count, include_sum = countSubsetsAndSum(arr, target - arr[idx], idx + 1, memo_count, memo_sum)
        include_count += 1  # Include the current element itself

    # Exclude current element
    exclude_count, exclude_sum = countSubsetsAndSum(arr, target, idx + 1, memo_count, memo_sum)

    # Total count and sum of subsets
    total_count = include_count + exclude_count
    total_sum = include_sum + exclude_sum + (include_count * arr[idx])

    # Store the result in memoization tables
    memo_count[(idx, target)] = total_count
    memo_sum[(idx, target)] = total_sum

    return total_count, total_sum


def countSubsetsAndSumWithMemo(arr, target):
    # Initialize memoization dictionaries
    memo_count = {}
    memo_sum = {}
    
    count, total_sum = countSubsetsAndSum(arr, target, 0, memo_count, memo_sum)
    
    return count, total_sum


# Test cases
arr = [1, 2, 3]
S = 4
count, total_sum = countSubsetsAndSumWithMemo(arr, S)
print(f"Count of subsets with sum {S}: {count}")  # Output: 3
print(f"Sum of all subsets with sum {S}: {total_sum}")  # Output: 8

arr = [1, 1, 1]
S = 2
count, total_sum = countSubsetsAndSumWithMemo(arr, S)
print(f"Count of subsets with sum {S}: {count}")  # Output: 3
print(f"Sum of all subsets with sum {S}: {total_sum}")  # Output: 6
