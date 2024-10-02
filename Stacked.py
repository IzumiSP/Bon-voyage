class Stack:
    def __init__(self, s):
        self.size = s
        self.arr = [0] * s
        self.top = -1

    def push(self, v):
        if not self.isFull():
            self.top += 1
            self.arr[self.top] = v
        else:
            print(f"Stack if full. Cannot push: {v}.")

    def pop(self):
        if not self.isEmpty():
            e = self.arr[self.top]
            self.top -= 1
            return e
        else:
            print("Stack is empty. Cannot pop.")
            return -1
        
    def peek(self):
        if self.top >= 0:
            e = self.arr[self.top]
            return e
        else:
            print("Stack is empty. Cannot peek.")
            return -1
        
    def isEmpty(self):
        return self.top == -1
    
    def isFull(self):
        return self.top >= self.size
        
if __name__ == "__main__":
    input_string = "Hello, World!"
    input_length = len(input_string)

    char_stack = Stack(101)

    # Push each character onto the stack
    for i in range(input_length):
        current_char = input_string[i]
        char_stack.push(current_char)

    # Pop the characters from the stack to construct the reversed string
    reversed_string = ""
    while not char_stack.isEmpty():
        reversed_string += char_stack.pop()

    print(reversed_string)