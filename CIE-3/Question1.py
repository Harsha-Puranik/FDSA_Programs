class Node:
    """Class to represent a node in a singly linked list."""
    def __init__(self, data):
        self.data = data  
        self.next = None 


class Stack:
    """Class to represent a stack using a singly linked list."""
    def __init__(self):
        self.top = None  

    def push(self, data):
        """Push a new element onto the stack."""
        new_node = Node(data) 
        new_node.next = self.top  
        self.top = new_node 

    def pop(self):
        """Remove and return the top element of the stack."""
        if self.empty():
            raise IndexError("Pop from an empty stack")
        popped_data = self.top.data  
        self.top = self.top.next  
        return popped_data

    def peek(self):
        """Return the top element of the stack without removing it."""
        if self.empty():
            raise IndexError("Peek from an empty stack")
        return self.top.data

    def empty(self):
        """Check if the stack is empty."""
        return self.top is None


# Example usage:
if __name__ == "__main__":
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)

    print("Top element (peek):", stack.peek())  
    print("Popped element:", stack.pop())      
    print("Popped element:", stack.pop())      
    print("Is stack empty?", stack.empty())   
    print("Popped element:", stack.pop())      
    print("Is stack empty?", stack.empty())  

Output:
/usr/bin/python3 /home/rvu/question1.py
Top element (peek): 30
Popped element: 30
Popped element: 20
Is stack empty? False
Popped element: 10
Is stack empty? True
