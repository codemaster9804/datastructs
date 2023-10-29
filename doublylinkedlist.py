class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def setNext(self, node):
        self.next = node

    def setPrev(self, node):
        self.prev = node

    def __repr__(self):
        return repr(self.data)

class DoublyLinkedList:
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

    def __reversed__(self):
        i = self.tail
        while i:
            yield i
            i = i.prev

    def addToTail(self, node):
        if not self:
            self.head = node
            self.tail = node
        else:
            self.tail.setNext(node)
            node.setPrev(self.tail)
            self.tail = node
        self.size += 1

    def addToHead(self, node):
        if not self:
            self.head = node
            self.tail = node
        else:
            node.setNext(self.head)
            self.head.setPrev(node)
            self.head = node
        self.size += 1

    def removeIndex(self, index):
        if not self or index > self.size -1:
            print("Index out of Bounds")
            return
        self.size -= 1
        if index == 0:
            if not self:
                self.head = None
                self.tail = None
                return
            self.head.next.setPrev(None)
            self.head = self.head.next
            return
        if index == self.size:
            self.tail.prev.setNext(None)
            self.tail = self.tail.prev
            return
        if (index > self.size /2):
            j = self.tail
            for i in range(self.size, index, -1):
                j = j.prev
        else:
            j = self.head
            for i in range(index):
                j = j.next
        
        j.prev.setNext(j.next)
        j.next.setPrev(j.prev)
            

                

    def remove(self, data):

        if not self:
            return
        for node in self:
            if node.data == data:
                if node.prev:
                    node.prev.setNext(node.next)
                else:
                    self.removeIndex(0)
                    continue
                if node.next:
                    node.next.setPrev(node.prev)
                else:
                    self.removeIndex(self.size -1)
                    continue
                self.size -= 1
            


    def find(self, data):
        for node in self:
            if node.data == data:
                return true

        return false

    def __repr__(self):
        ret = ""
        for node in self:
            ret += node.__repr__() + " <---> "
        return ret

# tests

mylist = DoublyLinkedList()
nodes = []
for i in range(20):
    nodes.append(Node(i))

for node in nodes:
    mylist.addToTail(node)

for node in reversed(mylist):
    print(node)