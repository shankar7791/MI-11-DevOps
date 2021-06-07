class Binary_tree :
    def __init__(self, data) :
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Binary_tree(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None :
                    self.right = Binary_tree(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data


    def tree(self):
        if self.left:
            self.left.tree()
        print(self.data),
        if self.right:
            self.right.tree()
print("the inserted elements of binary tree are: ")

root = Binary_tree(66)

root.insert(8)
root.insert(7)
root.insert(55)
root.insert(21)
root.insert(3)
root.insert(50)
root.tree()