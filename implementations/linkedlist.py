class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    
    def prepend(self, data):
        node = Node(data, self.head)
        self.head = node

    def append(self, data):
        if self.head == None:
            self.prepend(data)
            return
        
        current = self.head
        while current.next:
            current = current.next
        
        current.next = Node(data, None)

    def fromList(self, list):
        self.head = None
        
        for elem in list:
            self.append(elem)
        
    def length(self):
        current = self.head
        result = 0

        while current:
            current = current.next
            result += 1
        
        return result
    
    def removeAt(self, idx):
        if idx < 0 or idx > self.length() - 1:
            raise Exception("Invalid index")

        if idx == 0:
            self.head = self.head.next
            return

        current = self.head
        currentIdx = 0

        while current:
            if currentIdx == idx - 1:
                current.next = current.next.next
                break
            
            current = current.next
            currentIdx += 1

    def insertAt(self, idx, data):
        if idx < 0 or idx > self.length() - 1:
            raise Exception("Invalid index")
        
        if idx == 0:
            self.prepend(data)
        
        current = self.head
        currentIdx = 0

        while current:
            if currentIdx == idx - 1:
                current.next = Node(data, current.next)

            current = current.next
            currentIdx += 1

    def print(self):
        current = self.head

        while current:
            print(f"{current.data}", end=" -> ")
            current = current.next



def main():
    lilist = LinkedList()
    lilist.fromList([1,2,3,4,5])
    lilist.insertAt(4, 55)
    lilist.print()

if __name__ == "__main__":
    main()