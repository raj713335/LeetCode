#  Time Complexity: O(n * log(sum - max))


def is_possible(pages, m, max_pages):
    student_count = 1
    current_sum = 0

    for page in pages:
        if current_sum + page > max_pages:
            student_count += 1
            current_sum = page
            if student_count > m:
                return False
        else:
            current_sum += page
    return True

def allocate_min_pages(pages, m):
    if m > len(pages):
        return -1  # Not enough books for students

    low = max(pages)
    high = sum(pages)
    result = high

    while low <= high:
        mid = (low + high) // 2
        if is_possible(pages, m, mid):
            result = mid
            high = mid - 1
        else:
            low = mid + 1

    return result

# Example
pages = [12, 34, 67, 90]
students = 2
print(f"Minimum number of pages: {allocate_min_pages(pages, students)}")
