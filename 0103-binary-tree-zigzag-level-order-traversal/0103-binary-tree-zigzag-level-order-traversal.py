from collections import deque
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if not root:
            return []
        
        queue = deque([root])
        result = [] 
        level = 0       
        while queue:
            level_queue = []
            level +=1
            qlen = len(queue)
            for i in range(qlen):
                node = queue.popleft()
                if node:
                    queue.append(node.left)
                    queue.append(node.right)
                    level_queue.append(node.val)
            if level_queue:
                if level % 2 == 0:
                    result.append(level_queue[::-1])
                else:
                    result.append(level_queue)

        return result
