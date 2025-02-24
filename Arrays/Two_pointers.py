def two_pointer_sum(arr, target):
    left, right = 0, len(arr) - 1
    while left < right:
        curr_sum = arr[left] + arr[right]
        if curr_sum == target:
            return (left, right)  
        elif curr_sum < target:
            left += 1  
        else:
            right -= 1  
    return -1  

arr = [1, 2, 3, 4, 6, 8, 10]
target = 10
print(two_pointer_sum(arr, target))  
