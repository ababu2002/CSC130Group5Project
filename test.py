#from node import Node
from Tree import Tree
import json as js

def main():
    with open('new_monarchs.json', 'r') as file:
        monarchs = js.load(file)
    #print(js.dumps(monarchs, indent=4))
    print(monarchs['Children'][0]['Children'][0])


if __name__ == '__main__':
    main()