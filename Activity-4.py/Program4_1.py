class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
    
    # Method to append a node to the linked list
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            last_node = self.head
            while last_node.next:
                last_node = last_node.next
            last_node.next = new_node
    
    # Method to search for a node by value
    def search(self, data):
        current_node = self.head
        while current_node:
            if current_node.data == data:
                return True
            current_node = current_node.next
        return False
    
    # Method to display the linked list
    def display(self):
        if self.head is None:
            print("The list is empty.")
            return
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")

# Using Inputs
sll = SinglyLinkedList()

# Append nodes
sll.append(10)
sll.append(20)
sll.append(30)

# Search for a value in the list
search_value = 20
if sll.search(search_value):
    print(f"Node with value {search_value} found in the list.")
else:
    print(f"Node with value {search_value} not found in the list.")

search_value = 40
if sll.search(search_value):
    print(f"Node with value {search_value} found in the list.")
else:
    print(f"Node with value {search_value} not found in the list.")

# Display the list
print("Linked List after appending with values 10, 20, 30:")
sll.display()
