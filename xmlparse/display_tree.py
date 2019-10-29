import xml.etree.ElementTree as ET
import sys

def walk(root, i=0):
    text = str(root.text)
    if "\n" in text:
        text = text.replace("\n", "")
    text = " ".join(text.split())
    print((" " * 5)*i,"|-->", root.tag, root.attrib, text)
    i+=1
    for child in root:
        walk(child,i)

def display_tree(file):
    tree = ET.parse(file)
    root = tree.getroot()
    print(f"\nTree Data for {file}\n----------------------------")
    print(root.tag, root.attrib)
    for child in root:
        walk(child)

def main():
    for arg in sys.argv:
        try:
            display_tree(arg)
        except:
            print(f"{arg} cannot be walked")


if __name__ == "__main__":
    main()



