def kadane_algorithm(arr):
    max_sum = 0
    current_sum = 0  

    for num in arr:
        current_sum = max(num, current_sum + num) 
        max_sum = max(max_sum, current_sum)

    return max_sum

arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(kadane_algorithm(arr))  
