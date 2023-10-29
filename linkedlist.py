class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def setNext(self, node):
        self.next = node
    def __repr__(self):
        return repr(self.data)

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self):
        return self.size

    def __iter__(self):
        i = self.head
        while i:
            yield i
            i = i.next
    def __reversed__(self, node = None):
        if not self:
            return
        if not node:
            node = self.head
        if node.next == None:
            yield node
        else:
            yield from self.__reversed__(node.next)
            yield node
            

    def addToTail(self, node):
        if not self:
            self.head = node
            self.tail = node
        else:
            self.tail.setNext(node)
            self.tail = node
        self.size += 1

    def addToHead(self, node):
        if not self:
            self.head = node
            self.tail = node
        else:
            node.setNext(self.head)
            self.head = node
        self.size += 1

    def removeIndex(self, index):
        if (index == 0):
            self.head = self.head.next
            return
        i = 0
        for node in self:
            if index == i - 1:
                node.next = node.next.next
                if node.next == None:
                    self.tail = node
                return
            else:
                i += 1

    def remove(self, data):

        if self.head.data == data:
            removeIndex(0)
        
        for node in self:
            if node.next.data == data:
                node.next = node.next.next
                if node.next == None:
                    self.tail = node
                return

    def find(self, data):
        for node in self:
            if node.data == data:
                return true

        return false

    def __repr__(self):
        ret = ""
        for node in self:
            ret += node.__repr__() + " ---> "
        return ret

# tests

mylist = LinkedList()
nodes = []
for i in range(20):
    nodes.append(Node(i))

for node in nodes:
    mylist.addToTail(node)

for node in reversed(mylist):
    print(node)