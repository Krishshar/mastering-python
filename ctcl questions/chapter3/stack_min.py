import sys
class MinStack:
    def __init__(self):
        self.items = []
        self.mins = []
        
    def push(self, item):
        if self.is_empty():
            self.items.append(item)
            self.mins.append(item)
        else:
            self.items.append(item)
            self.mins.append(min(self.mins[-1], item))
    
    def pop(self):
        if self.is_empty():
            raise Exception('Stack is Empty')
        else:
            value = self.items.pop()
            self.mins.pop()
            return value
    
    def peek(self):
        if self.is_empty():
            raise Exception('Stack is Empty')
        return self.items[-1]
    
    def minimum(self):
        if not len(self.mins):
            return None
        return self.mins[-1]

    def is_empty(self):
        return len(self.items) == 0

if __name__ == "__main__":
    stack = MinStack()
    stack.push(2)
    stack.push(3)
    print(stack.minimum())
    stack.pop()
    stack.pop()
    stack.push(2)
    stack.push(5)
    print(stack.minimum())
