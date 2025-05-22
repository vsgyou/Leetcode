# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def isMirror(t1, t2):
            # 두 서브트리가 모두 None이면 대칭
            if not t1 and not t2:
                return True
            # 한쪽만 None이면 비대칭
            if not t1 or not t2:
                return False
            # 현재 노드 값이 같고, 서브트리가 대칭적이면 True
            return (t1.val == t2.val and 
                    isMirror(t1.left, t2.right) and 
                    isMirror(t1.right, t2.left))
        
        # 루트 노드의 좌우 서브트리를 비교
        return isMirror(root, root)

        # if not root:
        #     return None

        # stack = [(root.left, root.right)]
        # while stack:
        #     left, right = stack.pop()
        #     if not left and not right:
        #         continue
        #     if not left or not right:
        #         return False
        #     if left.val != right.val:
        #         return False
            
        #     stack.append((left.left, right.right))
        #     stack.append((left.right, right.left))

        # return True
            