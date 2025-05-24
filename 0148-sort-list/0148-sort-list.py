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
        
        # 중간을 찾는 함수
        def getMid(head):
            slow, fast = head, head.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow
        
        # 중간인덱스를 찾아
        mid = getMid(head)
        # 중간 인덱스 이후를 저장
        right = mid.next
        # 중간 인덱스의 next를 끊음
        mid.next = None
        # ex) 1->2->3->4->5->6
        # 1->2->3->None, 4->5->6->None

        left = self.sortList(head)
        # 1->2->None, 3->None
        right = self.sortList(right)
        # 4->5->None, 6->None
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
        