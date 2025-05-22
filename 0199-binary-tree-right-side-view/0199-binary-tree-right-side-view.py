from collections import deque
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """

        result = []
        queue = deque([root])

        while queue:
            rightside = None
            qlen = len(queue)   # 한 레벨에서의 개수

            for i in range(qlen):
                node = queue.popleft()
                print(node)
                if node:
                    rightside = node
                    queue.append(node.left)
                    queue.append(node.right)

            if rightside:
                result.append(rightside.val)
        return result