class OneDArray:
    def __init__(self, size):
        """Initialize an empty array with a given size."""
        self.array = [None] * size
        self.size = size
        self.count = 0
    
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
