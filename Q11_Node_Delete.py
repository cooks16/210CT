class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class List(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, n, x):
        # Not actually perfect: how do we prepend to an existing list?
        if n is not None:
            x.next = n.next
            n.next = x
            x.prev = n
            if x.next is not None:
                x.next.prev = x
        if self.head is None:
            self.head = self.tail = x
            x.prev = x.next = None
        elif self.tail == n:
            self.tail = x

    def display(self):
        values = []
        n = self.head
        while n is not None:
            values.append(str(n.value))
            n = n.next
        print("List: ", ",".join(values))

    def delete(self, x):
        n = self.head   # set to first value in list
        found = False
        while n.next.value is not None:   # loop through to find if value in list
            if n.next.value == x:
                found = True
                break
            else:
                n = n.next
        if found:
            n.next.next.prev = n   # set the item in list after to point to the item before
            n.next = n.next.next   # set the item in list before to point to item after

if __name__ == '__main__':
    l = List()
    l.insert(None, Node(4))
    l.insert(l.head, Node(6))
    l.insert(l.head, Node(8))
    l.insert(l.head, Node(9))
    l.insert(l.head, Node(3))
    l.insert(l.head, Node(5))
    l.insert(l.head, Node(7))
    l.display()
    l.delete(3)
    l.delete(5)
    l.display()
