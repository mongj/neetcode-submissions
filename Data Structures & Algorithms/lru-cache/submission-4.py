class Node:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def removeNode(self, node: Node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def appendNode(self, node: Node):
        prev = self.tail.prev
        tail_sentinel = self.tail
        prev.next = tail_sentinel.prev = node
        node.prev = prev
        node.next = tail_sentinel

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        # move the node to the end of the queue
        node = self.cache[key]
        self.removeNode(node)
        self.appendNode(node)
        return node.val

    def put(self, key: int, value: int) -> None:    
        if key in self.cache:
            self.removeNode(self.cache[key])
        self.cache[key] = Node(key, value)
        self.appendNode(self.cache[key])
        if len(self.cache) > self.capacity:
            lru_node = self.head.next
            self.removeNode(lru_node)
            self.cache.pop(lru_node.key)
