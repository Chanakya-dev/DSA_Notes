def max_sum_subarray(arr, k):
    n = len(arr)
    if n < k:
        return "Invalid input"

    max_sum = 0
    window_sum = sum(arr[:k])

    for i in range(n - k):
        window_sum = window_sum - arr[i] + arr[i + k]
        max_sum = max(max_sum, window_sum)

    return max_sum

arr = [2, 1, 5, 1, 3, 2]
k = 3
print(max_sum_subarray(arr, k))
