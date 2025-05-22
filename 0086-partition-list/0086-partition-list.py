# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: Optional[ListNode]
        :type x: int
        :rtype: Optional[ListNode]
        """
        small_node = ListNode(0)
        large_node = ListNode(0)
        small = small_node
        large = large_node

        curr = head
        if not head:
            return None
        while curr:
            if curr.val < x:
                small.next = curr
                small = small.next
            
            else:
                large.next = curr
                large = large.next
            curr = curr.next
        
        small.next = large_node.next
        large.next = None

        return small_node.next