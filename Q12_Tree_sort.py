class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Tree(object):
    def __init__(self):
        self.root = None

    def insert(self, x, y):
        if self.root is None:
            self.root = x
            x.left = None
            x.right = None
        elif x.value < y.value:
            if y.left is None:
                y.left = x
                print(y. value, y.left.value, "L")
            else:
                t.insert(x, y.left)
        else:
            if y.right is None:
                y.right = x
                print(y.value, y.right.value, "R")
            else:
                t.insert(x, y.right)

    def in_order(self):
        node = self.root
        values = []
        order = []
        empty = False

        while not empty:
            # continue to add values to list until no more values to left
            if node is not None:
                values.append(node)
                node = node.left
            else:
                if len(values) > 0:
                    node = values.pop()   # when no more values on the left remove final value
                    order.append(node.value)  # and place in ordered list
                    node = node.right  # set chosen node to the right of the last item removed
                    """ if node on the right is none on the next loop the value last in the list
                    will be selected and set the node will be set to the value on the right again
                    until the list is empty"""
                    """ if the node on the right has a value the the code will begin to work down
                    the left side of the list again"""
                else:
                    empty = True
                    print(order)

if __name__ == '__main__':
    t = Tree()
    t.insert(Node(5), None)
    t.insert(Node(2), t.root)
    t.insert(Node(7), t.root)
    t.insert(Node(8), t.root)
    t.insert(Node(6), t.root)
    t.insert(Node(9), t.root)
    t.insert(Node(1), t.root)
    t.insert(Node(0), t.root)
    t.insert(Node(3), t.root)
    t.insert(Node(4), t.root)
    t.in_order()
