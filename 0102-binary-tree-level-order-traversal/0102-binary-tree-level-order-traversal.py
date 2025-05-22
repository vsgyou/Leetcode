from collections import deque
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if not root:
            return []
        queue = deque([root])
        result = []
        while queue:
            qlen = len(queue)
            level_queue = []

            for i in range(qlen):
                node = queue.popleft()
                if node:
                    level_queue.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            if level_queue:
                result.append(level_queue)
        return result   