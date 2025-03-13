class DLinkedNode:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {} 
        self.capacity = capacity
        self.size = 0
        
        self.head = DLinkedNode()  
        self.tail = DLinkedNode() 
        self.head.next = self.tail
        self.tail.prev = self.head

    def _add_node(self, node):
        node.prev = self.head
        node.next = self.head.next
        
        self.head.next.prev = node
        self.head.next = node

    def _remove_node(self, node):
        prev = node.prev
        new = node.next
        
        prev.next = new
        new.prev = prev

    def _move_to_head(self, node):
        self._remove_node(node)
        self._add_node(node)

    def _pop_tail(self):
        res = self.tail.prev
        self._remove_node(res)
        return res

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._move_to_head(node) 
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._move_to_head(node)
        else:
            new_node = DLinkedNode(key, value)
            self.cache[key] = new_node
            self._add_node(new_node)
            self.size += 1
            
            if self.size > self.capacity:
                tail = self._pop_tail()
                del self.cache[tail.key]
                self.size -= 1

# Test cases
import unittest

class TestLRUCache(unittest.TestCase):
    def test_basic_operations(self):
        lRUCache = LRUCache(2)
        lRUCache.put(1, 1)  # cache is {1=1}
        lRUCache.put(2, 2)  # cache is {1=1, 2=2}
        self.assertEqual(lRUCache.get(1), 1)  # return 1
        lRUCache.put(3, 3)  # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
        self.assertEqual(lRUCache.get(2), -1)  # returns -1 (not found)
        lRUCache.put(4, 4)  # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
        self.assertEqual(lRUCache.get(1), -1)  # return -1 (not found)
        self.assertEqual(lRUCache.get(3), 3)  # return 3
        self.assertEqual(lRUCache.get(4), 4)  # return 4
    
    def test_update_existing(self):
        lRUCache = LRUCache(2)
        lRUCache.put(1, 1)
        lRUCache.put(2, 2)
        self.assertEqual(lRUCache.get(1), 1)
        lRUCache.put(1, 10)  # Update value for key 1
        self.assertEqual(lRUCache.get(1), 10)
        self.assertEqual(lRUCache.get(2), 2)
    
    def test_capacity_one(self):
        lRUCache = LRUCache(1)
        lRUCache.put(1, 1)
        lRUCache.put(2, 2)
        self.assertEqual(lRUCache.get(1), -1)
        self.assertEqual(lRUCache.get(2), 2)

if __name__ == "__main__":
    unittest.main()
