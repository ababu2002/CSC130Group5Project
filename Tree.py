from node import Node

class Tree(Node):
    def __init__(self, collection):
        self.children = []
        self.parent = None
        Node.__init__(self, collection)
    
    def add_child(self, child):
        Tree(child).parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        parent = self.parent
        while parent:
            level =+ 1
            parent = parent.parent
        return level
    
    def display(self):
        spaces = ' ' * self.get_level() * 3
        if self.parent:
            prefix = spaces + "|__"
        else:
            prefix = ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                Tree(child).display()
        
