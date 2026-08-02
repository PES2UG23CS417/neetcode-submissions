class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.cap = capacity
        self.left, self.right = Node(-1, -1), Node(-1, -1)
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, Node):
        oldLeft = Node.prev
        oldRight = Node.next
        oldLeft.next = oldRight
        oldRight.prev = oldLeft

    def insert(self, Node):
        oldRight = self.left.next
        self.left.next = Node
        oldRight.prev = Node
        Node.prev = self.left
        Node.next = oldRight

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            self.cache[key].value = value
        else:
            if self.cap != len(self.cache):
                self.cache[key] = Node(key, value)
                self.insert(self.cache[key])
            else:
                lru = self.right.prev
                self.remove(lru)
                del self.cache[lru.key]

                self.cache[key] = Node(key, value)
                self.insert(self.cache[key])
