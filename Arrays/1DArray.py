class OneDArray:
    def __init__(self, size):
        """Initialize an empty array with a given size."""
        self.array = [None] * size
        self.size = size
        self.count = 0
    
    def __str__(self):
        return str(self.array)
    def insert_at_end(self, value):
        """Insert an element at the end of the array."""
        if self.count < self.size:
            self.array[self.count] = value
            self.count += 1
        else:
            print("Array is full! Cannot insert.")
    
    def insert_at_begin(self, value):
        """Insert an element at the beginning of the array."""
        if self.count < self.size:
            for i in range(self.count, 0, -1):
                self.array[i] = self.array[i - 1]
            self.array[0] = value
            self.count += 1
        else:
            print("Array is full! Cannot insert.")
    
    def insert_at_index(self, index, value):
        """Insert an element at a specific index."""
        if 0 <= index <= self.count < self.size:
            for i in range(self.count, index, -1):
                self.array[i] = self.array[i - 1]
            self.array[index] = value
            self.count += 1
        else:
            print("Invalid index or array is full!")
    
    def delete_at_end(self):
        """Delete the last element."""
        if self.count > 0:
            self.array[self.count - 1] = None
            self.count -= 1
        else:
            print("Array is empty!")
    
    def delete_at_begin(self):
        """Delete the first element."""
        if self.count > 0:
            for i in range(self.count - 1):
                self.array[i] = self.array[i + 1]
            self.array[self.count - 1] = None
            self.count -= 1
        else:
            print("Array is empty!")
    
    def delete_at_index(self, index):
        """Delete an element at a specific index."""
        if 0 <= index < self.count:
            for i in range(index, self.count - 1):
                self.array[i] = self.array[i + 1]
            self.array[self.count - 1] = None
            self.count -= 1
        else:
            print("Invalid Index!")
    
    def update_value(self, index, value):
        """Update the value at a specific index."""
        if 0 <= index < self.count:
            self.array[index] = value
        else:
            print("Invalid Index!")
    
    def get(self, index):
        """Get the value at a specific index."""
        if 0 <= index < self.count:
            return self.array[index]
        else:
            print("Invalid Index!")
            return None
    
    def search_element(self, value):
        """Search for an element in the array and return its index."""
        for i in range(self.count):
            if self.array[i] == value:
                return i
        return -1  # Not found
    
    def display(self):
        """Display the array."""
        print("Array:", [self.array[i] for i in range(self.count)])

arra=OneDArray(5)
arra.insert_at_end(10)
arra.insert_at_end(20)
arra.insert_at_index(1,30)
arra.delete_at_end()
print(arra.search_element(10))
arra.display()