class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def get(self, index: int) -> int:
        if index >= self.length:
            return -1
        
        cur = self.head
        for _ in range(index):
            cur = cur.next
        
        return cur.val

    def insertHead(self, val: int) -> None:
        self.head = Node(val, self.head)
        if self.length == 0:
            self.tail = self.head

        self.length += 1

    def insertTail(self, val: int) -> None:
        new_node = Node(val)
        if self.length == 0:
            self.head = new_node
        else:
            self.tail.next = new_node

        self.tail = new_node
        self.length += 1

    def remove(self, index: int) -> bool:
        if index >= self.length:
            return False

        if index == 0:
            self.head = self.head.next
        else:
            cur = self.head
            for _ in range(index - 1):
                cur = cur.next
            
            if index == self.length - 1:
                cur.next = None
                self.tail = cur
            else:
                cur.next = cur.next.next
        
        self.length -= 1
        return True
        
    def getValues(self) -> List[int]:
        res = [None] * self.length
        cur = self.head
        for i in range(self.length):
            res[i] = cur.val
            cur = cur.next
        
        return res