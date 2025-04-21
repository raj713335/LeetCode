# Python Code to partition a set into two
# subsets such that the difference
# of subset sums is minimum

# Function to calculate the minimum absolute difference
def find_min_difference(arr, n, sum_calculated, sum_total):
    
    # Base case: if we've considered all elements
    if n == 0:
        return abs((sum_total - sum_calculated) 
                            - sum_calculated)

    # Include the current element in the subset
    include = find_min_difference(arr, n - 1, 
                    sum_calculated + arr[n - 1], sum_total)

    # Exclude the current element from the subset
    exclude = find_min_difference(arr,
                       n - 1, sum_calculated, sum_total)

    # Return the minimum of both choices
    return min(include, exclude)

# Function to get the minimum difference
def min_difference(arr):
    sum_total = 0
    
    # Calculate total sum of the array
    for num in arr:
        sum_total += num

    # Call recursive function to find 
    # the minimum difference
    return find_min_difference(arr, 
                           len(arr), 0, sum_total)

if __name__ == "__main__":

    arr = [1, 6, 11, 5]

    print(min_difference(arr))
