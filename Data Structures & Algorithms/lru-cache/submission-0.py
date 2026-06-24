class DLinkedL:
    def __init__(self, key=-1, val=-1, prev=None, next=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.nodes = {}
        self.head = None
        self.tail = None

    def get(self, key: int) -> int:
        if key not in self.nodes:
            return -1
        
        self.update(key)
        return self.nodes[key].val

    def put(self, key: int, value: int) -> None:
        if key not in self.nodes:
            if self.cap == len(self.nodes):
                del self.nodes[self.head.key]
                self.head = self.head.next
                if self.head == None:
                    self.tail == None
                else:
                    self.head.prev = None
            
            if len(self.nodes) == 0:
                self.nodes[key] = DLinkedL(key, value)
                self.head = self.tail = self.nodes[key]
                return  
            self.nodes[key] = DLinkedL(key, value, self.tail)
            self.tail.next = self.nodes[key]
            self.tail = self.tail.next
        else:
            self.nodes[key].val = value

        self.update(key)
    
    def update(self, key):
        if self.tail == self.nodes[key]:
            return 

        if self.head == self.nodes[key]:
            self.head = self.head.next
        else:
            self.nodes[key].prev.next = self.nodes[key].next

        self.nodes[key].next.prev = self.nodes[key].prev
        self.nodes[key].prev = self.tail
        self.tail.next = self.nodes[key]
        self.tail = self.tail.next
        self.tail.next = None

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)