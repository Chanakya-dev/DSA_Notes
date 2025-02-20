def two_pointer_sum(arr, target):
    left, right = 0, len(arr) - 1
    while left < right:
        curr_sum = arr[left] + arr[right]
        if curr_sum == target:
            return (left, right)  # Pair found
        elif curr_sum < target:
            left += 1  # Increase sum by moving left pointer
        else:
            right -= 1  # Decrease sum by moving right pointer
    return -1  # No pair found

arr = [1, 2, 3, 4, 6, 8, 10]
target = 10
print(two_pointer_sum(arr, target))  # Output: (2, 4)
