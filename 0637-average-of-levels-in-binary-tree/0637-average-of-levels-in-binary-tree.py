from collections import deque
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[float]
        """
        queue = deque([root])
        result = []

        while queue:
            qlen = len(queue)
            level_num = []
            for i in range(qlen):
                node = queue.popleft()

                if node:
                    level_num.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            if level_num:
                result.append(float(sum(level_num)) / float(len(level_num)))
                
        return result
