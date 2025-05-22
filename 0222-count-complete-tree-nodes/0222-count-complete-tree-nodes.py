# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def count(root):
    if not root:
        return 0
    return count(root.left)+count(root.right)+1
    
class Solution(object):

    def countNodes(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        return count(root)
