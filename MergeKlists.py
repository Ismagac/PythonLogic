from typing import List, Optional
import heapq

# Definition for singly-linked list node
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __repr__(self):
        return f"{self.val} -> {self.next}"

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        Merge k sorted linked lists into one sorted linked list.
        
        Args:
            lists: List of linked list heads
            
        Returns:
            Head of the merged sorted linked list
        """
        heap = []
        counter = 0
        
        for i, head in enumerate(lists):
            if head:
             
                heapq.heappush(heap, (head.val, counter, head))
                counter += 1
        
        dummy = ListNode(0)
        curr = dummy
        
        while heap:
            val, _, node = heapq.heappop(heap)
            
            curr.next = node
            curr = curr.next
            
            if node.next:
                heapq.heappush(heap, (node.next.val, counter, node.next))
                counter += 1
        
        return dummy.next
    
    def createLinkedList(self, arr: List[int]) -> Optional[ListNode]:
        if not arr:
            return None
        
        head = ListNode(arr[0])
        curr = head
        for val in arr[1:]:
            curr.next = ListNode(val)
            curr = curr.next
            
        return head

def main():
    solution = Solution()
    
    list1 = solution.createLinkedList([1, 4, 5])
    list2 = solution.createLinkedList([1, 3, 4])
    list3 = solution.createLinkedList([2, 6])
    
    result = solution.mergeKLists([list1, list2, list3])
    print(f"Merged list: {result}")

if __name__ == "__main__":
    main()
