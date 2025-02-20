## **📌 Arrays: A Complete Guide**  

### **🔹 What is an Array?**  
An **array** is a **collection of elements of the same data type**, stored in contiguous memory locations. It allows **random access** using an index.

### **🔹 Key Properties of Arrays**
✅ **Fixed Size** (in static arrays)  
✅ **Indexed Access** (O(1) time complexity for accessing elements)  
✅ **Efficient Traversal**  
✅ **Stores Homogeneous Data** (Same type elements)  

---

## **🔹 Types of Arrays**
1. **One-Dimensional Array (1D)**
   - Stores elements in a **single row**.  
   - Example: `arr = [10, 20, 30, 40]`  
   - Accessing an element: `arr[1]` → Output: `20`

2. **Two-Dimensional Array (2D)**
   - Stored in **rows and columns** (Matrix).  
   - Example:  
     ```
     arr = [
       [1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]
     ]
     ```
   - Accessing element: `arr[1][2]` → Output: `6`

3. **Multi-Dimensional Arrays (3D and more)**
   - Example: `arr[depth][row][column]`  

---

## **🔹 Basic Operations in Arrays**
| Operation     | Time Complexity | Explanation |
|--------------|---------------|-------------|
| **Access**  | O(1) | Directly access using index `arr[i]` |
| **Search**  | O(n) | Linear search takes O(n) time, Binary search takes O(log n) (sorted array) |
| **Insert**  | O(n) | If inserting at the end, O(1); inserting at the beginning or middle requires shifting (O(n)) |
| **Delete**  | O(n) | Deleting the last element is O(1), but shifting required for others (O(n)) |

---

## **🔹 Important Techniques on Arrays**
### **1️⃣ Kadane’s Algorithm (Maximum Subarray Sum)**
- Used to find the **maximum sum of a contiguous subarray**.
- **Time Complexity:** O(n)  
- **Example Problem:**  
   ```python
   def maxSubArray(nums):
       max_sum = nums[0]
       curr_sum = nums[0]

       for i in range(1, len(nums)):
           curr_sum = max(nums[i], curr_sum + nums[i])
           max_sum = max(max_sum, curr_sum)

       return max_sum

   print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))  # Output: 6
   ```

### **2️⃣ Two-Pointer Technique**
- **Used in problems like:** Finding pairs, reversing an array, etc.
- **Example Problem: Reverse an Array**
  ```python
  def reverseArray(arr):
      left, right = 0, len(arr) - 1
      while left < right:
          arr[left], arr[right] = arr[right], arr[left]
          left += 1
          right -= 1
      return arr

  print(reverseArray([1, 2, 3, 4, 5]))  # Output: [5, 4, 3, 2, 1]
  ```

### **3️⃣ Sliding Window Technique**
- Used for problems requiring **subarray processing**.
- **Example Problem: Maximum sum of a subarray of size k**
  ```python
  def maxSumSubarray(arr, k):
      max_sum, window_sum = 0, sum(arr[:k])
      for i in range(len(arr) - k):
          window_sum = window_sum - arr[i] + arr[i + k]
          max_sum = max(max_sum, window_sum)
      return max_sum

  print(maxSumSubarray([2, 1, 5, 1, 3, 2], 3))  # Output: 9
  ```

---

## **🔹 Common Array Problems**
1️⃣ **Find the Second Largest Element**  
2️⃣ **Find Duplicate in an Array**  
3️⃣ **Merge Two Sorted Arrays Without Extra Space**  
4️⃣ **Find Missing Number in an Array**  
5️⃣ **Majority Element in an Array**  
