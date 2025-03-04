class ThreeDArray:
    def __init__(self, depth, rows, cols):
        """Initialize a 3D array with given depth, rows, and columns."""
        self.depth = depth
        self.rows = rows
        self.cols = cols
        self.array = [[[None for _ in range(cols)] for _ in range(rows)] for _ in range(depth)]
    
    def insert_at_end(self, depth, row, value):
        """Insert an element at the end of a row in a specific depth."""
        if 0 <= depth < self.depth and 0 <= row < self.rows:
            for col in range(self.cols):
                if self.array[depth][row][col] is None:
                    self.array[depth][row][col] = value
                    return
            print("Row is full! Cannot insert.")
        else:
            print("Invalid depth or row index!")
    
    def insert_at_begin(self, depth, row, value):
        """Insert an element at the beginning of a row in a specific depth."""
        if 0 <= depth < self.depth and 0 <= row < self.rows:
            for col in range(self.cols - 1, 0, -1):
                self.array[depth][row][col] = self.array[depth][row][col - 1]
            self.array[depth][row][0] = value
        else:
            print("Invalid depth or row index!")
    
    def insert_at_index(self, depth, row, col, value):
        """Insert an element at a specific index in a row of a given depth."""
        if 0 <= depth < self.depth and 0 <= row < self.rows and 0 <= col < self.cols:
            if self.array[depth][row][col] is None:
                self.array[depth][row][col] = value
            else:
                # Shift elements to the right if there's space
                if self.array[depth][row][-1] is not None:
                    print("Row is full! Cannot insert.")
                    return
                for i in range(self.cols - 1, col, -1):
                    self.array[depth][row][i] = self.array[depth][row][i - 1]
                self.array[depth][row][col] = value
        else:
            print("Invalid depth, row, or column index!")
    
    def delete_at_end(self, depth, row):
        """Delete the last element in a row of a specific depth."""
        if 0 <= depth < self.depth and 0 <= row < self.rows:
            for col in range(self.cols - 1, -1, -1):
                if self.array[depth][row][col] is not None:
                    self.array[depth][row][col] = None
                    return
            print("Row is already empty!")
        else:
            print("Invalid depth or row index!")
    
    def delete_at_begin(self, depth, row):
        """Delete the first element in a row of a specific depth."""
        if 0 <= depth < self.depth and 0 <= row < self.rows:
            for col in range(self.cols - 1):
                self.array[depth][row][col] = self.array[depth][row][col + 1]
            self.array[depth][row][self.cols - 1] = None
        else:
            print("Invalid depth or row index!")

    def delete_at_index(self, depth, row, col):
        """Delete an element at a specific index in a row of a given depth."""
        if 0 <= depth < self.depth and 0 <= row < self.rows and 0 <= col < self.cols:
            if self.array[depth][row][col] is None:
                print("No element to delete at the given index.")
            else:
                for i in range(col, self.cols - 1):
                    self.array[depth][row][i] = self.array[depth][row][i + 1]
                self.array[depth][row][self.cols - 1] = None
        else:
            print("Invalid depth, row, or column index!")

    def update(self, depth, row, col, value):
        """Update the value at a specific position."""
        if 0 <= depth < self.depth and 0 <= row < self.rows and 0 <= col < self.cols:
            self.array[depth][row][col] = value
        else:
            print("Invalid position!")
    
    def get(self, depth, row, col):
        """Get the value from a specific position."""
        if 0 <= depth < self.depth and 0 <= row < self.rows and 0 <= col < self.cols:
            return self.array[depth][row][col]
        else:
            print("Invalid position!")
            return None
    
    def search(self, value):
        """Search for an element in the 3D array."""
        for d in range(self.depth):
            for r in range(self.rows):
                for c in range(self.cols):
                    if self.array[d][r][c] == value:
                        return (d, r, c)
        return -1  # Not found
    
    def display(self):
        """Display the 3D array."""
        for d in range(self.depth):
            print(f"Depth {d}:")
            for row in self.array[d]:
                print(row)
            print()

# Example Usage
three_d_array = ThreeDArray(2, 3, 3)

# Insert values
three_d_array.insert_at_end(0, 0, 5)
three_d_array.insert_at_begin(1, 1, 10)
three_d_array.insert_at_index(1, 1, 1, 20)
three_d_array.insert_at_index(0, 2, 2, 30)

# Display
three_d_array.display()

# Delete values
three_d_array.delete_at_end(0, 0)
three_d_array.delete_at_begin(1, 1)
three_d_array.delete_at_index(1, 1, 1)

# Display after deletion
three_d_array.display()
