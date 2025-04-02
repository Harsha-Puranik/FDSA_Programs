class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = self.rear = None

    def Enqueue(self, data):
        new_node = Node(data)
        if self.rear is None:
            self.front = self.rear = new_node
            return
        else:
            self.rear.next = new_node
            self.rear = new_node
        print(f'Enqueued item is {self.rear.data}')

q = Queue()
q.Enqueue(20)
q.Enqueue(30)
q.Enqueue(40)

Output :
Enqueued item is 30
Enqueued item is 40
