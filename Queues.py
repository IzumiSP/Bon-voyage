class Queue:
    def __init__(self, s):
        self.capacity = s
        self.q = [None] * s
        self.front = 0
        self.rear = 0
        self.size = 0

    def enqueue(self, v):
        if self.size == self.capacity:
            raise Exception("Queue is full")
        self.q[self.rear] = v
        self.rear = (self.rear + 1) % self.capacity
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            return None
        item = self.q[self.front]
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return item

    def peek(self):
        if not self.isEmpty():
            return None
        return self.q[self.front]

    def isEmpty(self):
        return self.size == 0
    
    def getSize(self):
        return self.size
    
arr = Queue(10)
arr.enqueue(1)
arr.enqueue(2)
arr.enqueue(3)
arr.enqueue(4)
arr.enqueue(5)
arr.enqueue(6)
arr.enqueue(7)
arr.dequeue()
print(arr)