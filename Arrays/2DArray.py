class TwoDArray:
    def __init__(self, rows, cols):
        """Initialize a 2D array with given rows and columns."""
        self.rows = rows
        self.cols = cols
        self.array = [[None for _ in range(cols)] for _ in range(rows)]

    def insert_at_end(self, row, value):
        """Insert an element at the end of a row."""
        if 0 <= row < self.rows:
            for col in range(self.cols):
                if self.array[row][col] is None:
                    self.array[row][col] = value
                    return
            print("Row is full! Cannot insert.")
        else:
            print("Invalid row index!")

    def insert_at_begin(self, row, value):
        """Insert an element at the beginning of a row."""
        if 0 <= row < self.rows:
            for col in range(self.cols - 1, 0, -1):
                self.array[row][col] = self.array[row][col - 1]
            self.array[row][0] = value
        else:
            print("Invalid row index!")

    def insert_at_index(self, row, col, value):
        """Insert an element at a specific index by shifting elements to the right."""
    
        if not (0 <= row < self.rows and 0 <= col < self.cols):
            print("Invalid row or column index!")
            return

        if self.array[row][-1] is not None:
            print("Row is full! Cannot insert.")
            return

        for i in range(self.cols - 1, col, -1):
            self.array[row][i] = self.array[row][i - 1]
        self.array[row][col] = value

    def delete_at_end(self, row):
        """Delete the last element in a row."""
        if 0 <= row < self.rows:
            for col in range(self.cols - 1, -1, -1):
                if self.array[row][col] is not None:
                    self.array[row][col] = None
                    return
            print("Row is already empty!")
        else:
            print("Invalid row index!")

    def delete_at_begin(self, row):
        """Delete the first element in a row."""
        if 0 <= row < self.rows:
            for col in range(self.cols - 1):
                self.array[row][col] = self.array[row][col + 1]
            self.array[row][self.cols - 1] = None
        else:
            print("Invalid row index!")

    def delete_at_index(self, row, col):
        """Delete an element at a specific index by shifting elements left."""
        if 0 <= row < self.rows and 0 <= col < self.cols:
            for i in range(col, self.cols - 1):
                self.array[row][i] = self.array[row][i + 1]
                self.array[row][self.cols - 1] = None
        else:
            print("Invalid position!")


    def update(self, row, col, value):
        """Update the value at a specific position."""
        if 0 <= row < self.rows and 0 <= col < self.cols:
            self.array[row][col] = value
        else:
            print("Invalid position!")

    def get(self, row, col):
        """Get the value from a specific position."""
        if 0 <= row < self.rows and 0 <= col < self.cols:
            return self.array[row][col]
        else:
            print("Invalid position!")
            return None

    def search(self, value):
        """Search for an element in the 2D array."""
        for i in range(self.rows):
            for j in range(self.cols):
                if self.array[i][j] == value:
                    return (i, j)
        return -1  # Not found

    def display(self):
        """Display the 2D array."""
        for row in self.array:
            print(row)


# Testing the 2D array operations
two_d_array = TwoDArray(3, 3)

# Insert elements
two_d_array.insert_at_end(0, 5)
two_d_array.insert_at_begin(1, 10)
two_d_array.insert_at_end(2, 15)
two_d_array.insert_at_index(1, 1, 20)

# Display current state
print("Initial 2D Array:")
two_d_array.display()

# Delete operations
two_d_array.delete_at_end(0)
two_d_array.delete_at_begin(1)
two_d_array.delete_at_index(2, 0)

# Display after deletions
print("\nAfter Deletions:")
two_d_array.display()

# Search and Get operations
print("\nSearch for 20:", two_d_array.search(20))
print("Get value at (1,1):", two_d_array.get(1, 1))

# Update an element
two_d_array.update(2, 2, 50)
print("\nAfter Updating (2,2) with 50:")
two_d_array.display()
