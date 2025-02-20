def kadane_algorithm(arr):
    max_sum = float('-inf')  # Store the maximum sum found
    current_sum = 0  # Store the sum of the current subarray

    for num in arr:
        current_sum = max(num, current_sum + num)  # Either start new or extend current subarray
        max_sum = max(max_sum, current_sum)  # Update max sum

    return max_sum

arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(kadane_algorithm(arr))  # Output: 6 (subarray: [4, -1, 2, 1])
