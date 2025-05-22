# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: Optional[TreeNode]
        """
        if not inorder or not postorder:
            return None
    
        root_val = postorder.pop()
        root = TreeNode(root_val)

        mid_index = inorder.index(root_val)
        root.right = self.buildTree(inorder[mid_index+1:], postorder)
        root.left = self.buildTree(inorder[:mid_index], postorder)
        return root