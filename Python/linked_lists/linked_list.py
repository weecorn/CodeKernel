class Node:
    """Class representing a single node in a linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """Class representing the linked list."""
    def __init__(self):
        self.head = None

    def append(self, data):
        """Add a new node at the end of the linked list."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def print_list(self):
        """Print the linked list."""
        current = self.head
        while current:
            print(f"{current.data} -> ", end="")
            current = current.next
        print("None")

    def delete_list(self):
        """Delete the entire linked list."""
        self.head = None
        print("Linked list deleted.")


# Example usage
if __name__ == "__main__":
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)

    print("Linked List:")
    ll.print_list()

    ll.delete_list()
