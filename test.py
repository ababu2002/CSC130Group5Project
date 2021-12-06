#from node import Node
from Tree import Tree
import json as js

def main():
    with open('new_monarchs.json', 'r') as file:
        monarchs = js.load(file)
    monarch = Tree(monarchs["Name"])
    for child in monarchs["Children"]:
        monarch.add_child(child["Name"])
    monarch.display()
    print(monarch.children)

if __name__ == '__main__':
    main()