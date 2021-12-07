import json as js

def main():
    with open('new_monarchs.json', 'r') as file:
        monarchs = js.load(file)

        print(monarchs["Name"])
        print(monarchs["Marriage"])
        for child in monarchs["Children"]:
            print(child["Name"])


if __name__ == '__main__':
    main()