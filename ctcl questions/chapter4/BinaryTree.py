class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    def insert(self, value):
        if self:
            if self.value >= value:
                if self.left is None:
                    self.left = BinaryTreeNode(value)
                else:
                    self.left.insert(value)
            else:
                if self.right is None:
                    self.right = BinaryTreeNode(value)
                else:
                    self.right.insert(value)
    
    def inorder(self):
        if self:
            if self.left:
                self.left.inorder()
            print(self.value)
            if self.right:
                self.right.inorder()

if __name__ == "__main__":
    b = BinaryTreeNode(10)
    b.insert(5)
    b.insert(2)
    b.insert(8)
    b.inorder()
