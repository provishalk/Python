import random


class BinaryTree:
    root = None

    class Node:
        def __init__(self, x):
            self.value = x
            self.left = None
            self.right = None

    def insert(self, value):
        to_add = self.Node(value)

        if self.root is None:
            self.root = to_add
            return
        temp = self.root
        while temp is not None:
            if value <= temp.value:
                if temp.left is None:
                    temp.left = to_add
                    return
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = to_add
                    return
                temp = temp.right

    def triverse(self):
        temp = self.root
        if temp is None:
            print("Tree is Empty")
            return
        def node(temp):
            if temp is not None:
                node(temp.left)
                print(temp.value)
                node(temp.right)
        node(temp)


if __name__ == '__main__':
    numbers = BinaryTree()
    list = [10, 20, 3, 5, 0, 15, 1000, 25, 4, 1, 2, 3, 4]
    for i in list:
        numbers.insert(i)
    numbers.triverse()