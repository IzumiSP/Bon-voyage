class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_front(self, value):
        new_node = Node(value)
        new_node.next = self.head

        self.head = new_node

    def get_head_value(self):
        if self.head is None:
            return -1
        else:
            return self.head.value
        
    def insert_end(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return

        self.tail.next = new_node
        self.tail = new_node

    def get_last_value(self):
        if self.head is None:
            return -1
            
        current = self.head
        while current.next:
            current = current.next
        return current.value
    
    def insert_after_k(self, value, k):
        new_node = Node(value)
        current = self.head

        if current is None:
            self.head = new_node
            return

        for _ in range(k - 1):
            current = current.next

        new_node.next = current.next
        current.next = new_node

    def print_values(self):
        current = self.head
        while current:
            print(current.value, end=" ")
            current = current.next
        print()

    def deleteNode(self, value):
        if self.head.value == value:
            self.head = self.head.next
            return
        
        iter = self.head

        while iter.next:
            if iter.next.value == value:
                iter.next = iter.next.next
                return
            iter = iter.next

link = LinkedList()
vals = list(map(int, input().split()))
for x in vals:
    link.insert_end(x)

link.print_values()
link.deleteNode(3)
link.print_values()