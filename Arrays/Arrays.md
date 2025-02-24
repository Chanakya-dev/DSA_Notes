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
### **1️⃣ One-Dimensional Array (1D)**
- Stores elements in a **single row**.  
- Example: `arr = [10, 20, 30, 40]`  
- Accessing an element: `arr[1]` → Output: `20`  

### **2️⃣ Two-Dimensional Array (2D)**
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

### **3️⃣ Multi-Dimensional Arrays (3D and more)**
- Arrays with more than two dimensions, commonly used in graphics, scientific computing, and data processing.
- Example: `arr[depth][row][column]`  

---

## **🔹 Basic Operations in Arrays**
| **Operation**   | **Time Complexity** | **Explanation** |
|---------------|-----------------|----------------|
| **Access**   | O(1)  | Directly access using index `arr[i]`. |
| **Search**   | O(n)  | Linear search in unsorted arrays takes O(n); Binary search in sorted arrays takes O(log n). |
| **Insert**   | O(n)  | Inserting at the end takes O(1), but inserting at the beginning or middle requires shifting elements (O(n)). |
| **Delete**   | O(n)  | Deleting the last element is O(1), but deleting from the beginning or middle requires shifting (O(n)). |

---

## **🔹 Common Array Operations**
### **1️⃣ Traversing an Array**
- Visiting each element of an array sequentially.

### **2️⃣ Searching an Element**
- **Linear Search** (O(n)) for unsorted arrays.  
- **Binary Search** (O(log n)) for sorted arrays.

### **3️⃣ Insertion in an Array**
- Inserting at the **end** → O(1).  
- Inserting at the **beginning or middle** → O(n) (requires shifting).  

### **4️⃣ Deletion from an Array**
- Deleting from the **end** → O(1).  
- Deleting from the **beginning or middle** → O(n) (requires shifting).  

### **5️⃣ Updating an Element**
- Updating an element at a given index is **O(1)** since arrays allow direct access.

---

## **🔹 Advantages of Arrays**
✅ **Fast Access** (O(1) time complexity for accessing elements).  
✅ **Memory Efficiency** (Uses contiguous memory allocation).  
✅ **Easy to Implement** for basic data storage and manipulation.  

## **🔹 Disadvantages of Arrays**
❌ **Fixed Size** (Cannot be dynamically resized in static arrays).  
❌ **Insertion & Deletion are Costly** (O(n) in the worst case).  
❌ **Wasted Space** (If the declared size is larger than needed).  

---

## **🔹 Applications of Arrays**
✔ Used in **searching & sorting algorithms**.  
✔ Used in **matrix operations** (2D arrays).  
✔ Used in **graph representations** (Adjacency matrix).  
✔ Used in **image processing** (Pixels stored as 2D arrays).  
✔ Used in **dynamic programming** (Storing intermediate results).