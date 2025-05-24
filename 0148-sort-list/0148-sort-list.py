# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return head
        
        def getMid(head):
            slow, fast = head, head.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow
        
        mid = getMid(head)
        right = mid.next
        mid.next = None

        left = self.sortList(head)
        right = self.sortList(right)

        def merge(left, right):
            dummy = ListNode()
            tail = dummy
            while left and right:
                if left.val < right.val:
                    tail.next = left
                    left = left.next
                else:
                    tail.next = right
                    right = right.next
                tail = tail.next
            tail.next = left if left else right
            return dummy.next
        return merge(left, right)
        