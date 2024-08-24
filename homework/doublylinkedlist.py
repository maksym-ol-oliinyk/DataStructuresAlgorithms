class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class DoublyLinkedList:
        def __init__(self):
            self.head = None
            self.prev = None

        def prepend(self, data):
            if not self.head:
                self.head = Node(data, None, None)
                return
            
            node = Node(data, self.head, None)
            self.head.prev = node
            self.head = node
        
        def append(self, data):
            if not self.head:
                self.prepend(data)
                return

            current = self.head
            while current.next:
                current = current.next
            
            current.next = Node(data, None, current)

        def fromList(self, list):
            self.head = None
            self.prev = None

            for elem in list:
                self.append(elem)
        
        def length(self):
            counter = 0
            current = self.head

            while current:
                current = current.next
                counter += 1

            return counter
        
        def removeAt(self, idx):
            if idx < 0 or idx >= self.length():
                raise Exception("index not valid")
            
            if idx == 0:
                self.head = self.head.next
                self.head.prev = None
                return
            
            current = self.head
            currentIdx = 0

            while current:
                if currentIdx == (idx - 1):
                    if current.next.next:
                        current.next.next.prev = current
                    current.next = current.next.next

                current = current.next
                currentIdx += 1

        def insertAt(self, idx, data):
            if idx < 0 or idx >= self.length():
                raise Exception("index not valid")
            
            if idx == 0:
                self.prepend(data)
                return 
            
            current = self.head
            currentIdx = 0

            while current:
                if currentIdx == (idx - 1):
                    node = Node(data, current.next, current)
                    current.next.prev = node
                    current.next = node

                current = current.next
                currentIdx += 1
                
        def print(self):
            current = self.head

            while current:
                print(f"{current.data} (prev {current.prev.data if current.prev else "empty"})", end=" -> ")
                current = current.next

        def print_forward(self):
            self.print()
        
        def print_backward(self):
            current = self.head
            while current.next:
                current = current.next 

            #got to last node, now reverse

            while current:
                print(f"{current.data}", end=" --> ")
                current = current.prev


def main():
    dllist = DoublyLinkedList()
    dllist.prepend(4)
    dllist.prepend(3)
    dllist.prepend(2)
    dllist.prepend(1)
    dllist.append(5)
    dllist.print_forward()
    print()
    dllist.print_backward()

if __name__ == "__main__":
    main()
        
