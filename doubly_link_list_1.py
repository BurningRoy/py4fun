# Operations of doubly linked list
# Every node consists of data, pointer to left, pointer to right

class Node:
    def __init__(self, data = None):
        self.data = data
        self.left = None
        self.right = None

class DoublyList:
    def __init__(self, node):
        self.head = None
        self.bottom = None
        self.current = None

        for i in node:
            self.append(Node(i))
        
    def __left(self):
        if self.current != self.head:
            self.current = self.current.left
        else:
            raise IndexError
        
    def __right(self):
        if self.current != self.bottom:
            self.current = self.current.right
        else:
            raise IndexError
    
    def append(self, node):
        if self.bottom != None:
            node.left = self.bottom
            self.bottom.right = node
            self.bottom = node
            self.current = self.bottom
        else:
            self.head = self.bottom = self.current = node
    
    def getfirst(self):
        return self.head

    def getlast(self):
        return self.bottom

    def getcurrent(self):
        return self.current

    def insert(self, node, offset = 0, start = 1):
        self.__seek(offset, start)
        self.__insert(node)

    def delete(self, offset = 0, start = 1):
        self.__seek(offset, start)
        self.__delete()

    def __seek(self, offset, start):
        if self.current is None:
            raise "Insert failed! There is no existing node in the list."
        if offset < 0 and start != 1:
            raise "offset should be positive when start is 0 and 2!"
        current_bak = self.current
        abs_offset = abs(offset)
        try:
            if start == 0:
                self.current = self.head
                while abs_offset > 0:
                    self.__right()
                    abs_offset -= 1
            elif start == 1:
                if offset < 0:
                    while abs_offset > 0:
                        self.__left()
                        abs_offset -= 1
                else:
                    while abs_offset > 0:
                        self.__right()
                        abs_offset -= 1
            elif start == 2:
                self.current = self.bottom
                while abs_offset > 0:
                    self.__left()
                    abs_offset -= 1
        except IndexError as ie:
            self.current = current_bak
            raise ie

    def __insert(self, node):
        node.left = self.current.left
        node.left.right = node
        node.right = self.current
        self.current.left = node
        self.__left()

    def __delete(self):
        self.current.right.left = self.current.left
        self.current.left.right = self.current.right
        bak = self.current
        self.__right()
        del bak

    def __str__(self):
        bak = self.current
        self.current = self.head
        nodes = []
        try:
            while True:
                nodes.append(self.current.data)
                self.__right()
        except IndexError as ie:
            self.current = bak
        return repr(nodes)

        
if __name__ == '__main__':
    dl = DoublyList([1,2,3,4,5])
    
        
