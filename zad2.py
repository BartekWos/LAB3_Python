
class Tree:
    def __init__(self, data):
        self.leftEdge = None
        self.rightEdge = None
        self.left = None
        self.right = None
        self.data = data

    #Insert into node or create a new one
    def InsertNode(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Tree(data)
                else:
                    self.left.InsertNode(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Tree(data)
                else:
                    self.right.InsertNode(data)
        else:
            self.data = data

    def Traverse(self):
        values = []
        values.append(self.data)
        if self.left:
            values.extend(self.left.Traverse())
        if self.right:
            values.extend(self.right.Traverse())
        return values

    @property
    def minimum(self):
        print("property")
        return min(self.Traverse())

    def __str__(self):
        if self.left:
            left = self.left.data
        else:
            left = None
        if self.right:
            right = self.right.data
        else:
            right = None
        return f"Node value is {self.data}, LeftChildNode is ({left}), RightChildNode is ({right})!"



root = Tree(10)
root.InsertNode(11)
root.InsertNode(4)
root.InsertNode(23)
root.InsertNode(54)
print(root.Traverse())
print(root.minimum)



