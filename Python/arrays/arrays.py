class Array:
    def __init__(self, capacity):
        self.data = [None] * capacity  # Initialize the array with None values
        self.size = 0  # Current number of elements
        self.capacity = capacity  # Maximum capacity of the array

    def insert(self, element):
        if self.size >= self.capacity:
            print("Array is full! Cannot insert element.")
            return
        self.data[self.size] = element
        self.size += 1

    def delete(self, index):
        if index < 0 or index >= self.size:
            print("Invalid index!")
            return
        for i in range(index, self.size - 1):
            self.data[i] = self.data[i + 1]
        self.data[self.size - 1] = None  # Clear the last element
        self.size -= 1

    def display(self):
        if self.size == 0:
            print("Array is empty!")
            return
        print("Array elements:", self.data[:self.size])

# Example usage
if __name__ == "__main__":
    # Initialize an array with a capacity of 10
    arr = Array(10)

    # Insert elements into the array
    arr.insert(5)
    arr.insert(10)
    arr.insert(15)

    # Display the array contents
    arr.display()

    # Delete an element at index 1
    arr.delete(1)

    # Display the array contents again
    arr.display()
