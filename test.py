#from node import Node
from Tree import Tree
import json as js

def main():
    with open('new_monarchs.json', 'r') as file:
        monarchs = js.load(file)
    root_monarch = Tree(monarchs)
    add_monarchs(root_monarch, monarchs['Children'])
    root_monarch.display()

def add_monarchs(tree_node, monarcha):
    if monarcha == None:
        return
    for monarch in monarcha:
        child_monarch = Tree(monarch)
        tree_node.add_child(child_monarch)
        add_monarchs(child_monarch, monarch['Children'])

if __name__ == '__main__':
    main()