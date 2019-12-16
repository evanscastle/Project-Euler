class Node:
    def __init__(self, data):
        self.parent = None
        self.children = []
        self.data = data
        self.name = None

    def give_name(self, name):
        self.name = name

    def give_data(self, new_data):
        self.data = new_data

    def give_parent(self, parent):
        assert isinstance(parent, Node)
        self.parent = parent

    def get_parent(self):
        return self.parent

    def give_child(self, child):
        assert isinstance(child, Node)
        self.children.append(child)

    def give_children(self, children):
        assert isinstance(child, Node)
        self.children = self.children + children

    def get_children(self):
        return self.children

    def print(self):
        print("Name:", self.name,"\nData:", self.data, "\n")

class Tree:
    def __init__(self):
        root = Node(None)
        self.children = []

    def give_child(self, child):
        assert isinstance(child, Node)
        self.children.append(child)



a = Node(1)
a.give_name("Node A")
a.print()
