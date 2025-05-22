class Solution:
    def buildTree(self, preorder, inorder):
        if not preorder or not inorder:
            return None
        
        root_val = preorder.pop(0)
        root = TreeNode(root_val)

        mid_index = inorder.index(root_val)
        root.left = self.buildTree(preorder, inorder[:mid_index])
        root.right = self.buildTree(preorder, inorder[mid_index+1:])

        return root