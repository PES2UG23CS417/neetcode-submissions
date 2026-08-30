class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity):
        self.cap = capacity
        self.cache = {}
        self.head, self.tail = Node(-1, -1), Node(-1, -1)
        self.head.next, self.tail.prev = self.tail, self.head
    
    def insert(self, node):
        # insert at the tail
        self.left, self.right = self.tail.prev, self.tail
        self.left.next = self.right.prev = node
        node.prev, node.next = self.left, self.right
    
    def remove(self, node):
        self.left, self.right = node.prev, node.next
        self.left.next, self.right.prev = self.right, self.left
    
    def get(self, key):
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        
        return -1
    
    def put(self, key, value):
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
    
        if len(self.cache) > self.cap:
            # we have to remove lru element
            lru = self.head.next
            self.remove(lru)
            del self.cache[lru.key] 