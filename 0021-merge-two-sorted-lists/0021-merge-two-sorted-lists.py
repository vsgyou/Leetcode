# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode()
        current = dummy

        while list1 or list2:
            if list1:
                val1 = list1.val
            else:
                val1 = 102
            
            if list2:
                val2 = list2.val
            else:
                val2 = 102
            
            if val1 < val2:
                current.next = ListNode(val1)
                current = current.next
                list1 = list1.next
            
            else:
                current.next = ListNode(val2)
                current = current.next
                list2 = list2.next
        return dummy.next
            