class MultiStacks:
    def __init__(self, stacksize = 5):
        self.num_stacks = 3
        self.items = [0] * (self.num_stacks * stacksize)
        self.size = [0] * (self.num_stacks)
        self.stacksize = stacksize

    def index_of_top(self, stack_num):
        offset = (self.num_stacks * stack_num)
        return self.size[stack_num] + offset - 1

    def push(self, item, stack_num):
        if self.is_full(stack_num):
            raise Exception('Stack is Full')
        self.size[stack_num] += 1
        self.items[self.index_of_top(stack_num)] = item
    
    def pop(self, stack_num):
        if self.is_empty(stack_num):
            raise Exception('Stack is Empty')
        top = self.index_of_top(stack_num)
        value = self.items[top]
        self.size[stack_num] -= 1
        self.items[top] = 0
        return value
    
    def peek(self, stack_num):
        if self.is_empty(stack_num):
            raise Exception('Stack is Empty')
        top = self.index_of_top(stack_num)
        value = self.items[top]
        return value

    def is_full(self, stack_num):
        return self.size[stack_num] == self.stacksize

    def is_empty(self, stack_num):
        return self.size[stack_num] == 0
       
if __name__ == "__main__":
    newstack = MultiStacks(2)
    print(newstack.is_empty(1))
    newstack.push(3, 1)
    print(newstack.peek(1))
    print(newstack.is_empty(1))
    newstack.push(2, 1)
    print(newstack.peek(1))
    print(newstack.pop(1))
    print(newstack.peek(1))
    newstack.push(3, 1)