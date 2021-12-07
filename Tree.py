from node import Node

class Tree(Node):
    def __init__(self, root):
        self.children = []
        self.parent = None
        Node.__init__(self, root)
    
    def add_child(self, child):
        self.children.append(child)
        child.parent = self
                
    def display(self, level=0):
        line = '      ' * level
        if level > 0: 
            line += "|__"
        line += self.data["Name"]
        if self.data["Marriage"]:
            line += "<-->" + self.data["Marriage"]
        print(line)
        for child in self.children:
            child.display(level + 1) 
