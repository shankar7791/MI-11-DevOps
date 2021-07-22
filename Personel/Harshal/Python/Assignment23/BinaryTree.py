class Binary_tree_node :
    def __init__(self, data) :
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Binary_tree_node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None :
                    self.right = Binary_tree_node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data


    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data),
        if self.right:
            self.right.PrintTree()
print("Binary Tree : Insert elements & print Binary Tree -")

root = Binary_tree_node(10)

root.insert(5)
root.insert(3)
root.insert(13)
root.insert(16)
root.insert(8)
root.insert(50)
root.PrintTree()