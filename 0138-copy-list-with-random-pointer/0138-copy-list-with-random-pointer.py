class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None
        
        current = head
        while current:
            copy = Node(current.val)
            copy.next = current.next
            current.next = copy
            current = copy.next
        current = head
        while current:
            if current.random:
                current.next.random = current.random.next
            current = current.next.next
        
        original = head
        copy_head = head.next
        copy = copy_head
        while original:
            original.next = original.next.next
            if copy.next:
                copy.next = copy.next.next
            original = original.next
            copy = copy.next
        return copy_head
            