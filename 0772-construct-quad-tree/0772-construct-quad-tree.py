"""
# Definition for a QuadTree node.
class Node(object):
    def __init__(self, val=False, isLeaf=False, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution(object):
    def construct(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: Node
        """
        def connection(currentSize, rs, cs):
            node = Node(False, False, None, None, None, None)
            initial = grid[rs][cs]
            cnt = 0
            for r in range(rs, rs+currentSize):
                for c in range(cs, cs+currentSize):
                    if grid[r][c] == initial:
                        cnt += 1
            
            half = currentSize // 2

            if cnt == currentSize ** 2:
                node.val = grid[rs][cs]
                node.isLeaf = True
            elif currentSize != 1:
                node.val = True
                node.isLeaf = False
                node.topLeft = connection(half, rs, cs)
                node.topRight = connection(half, rs, cs + half)
                node.bottomLeft = connection(half, rs + half, cs)
                node.bottomRight = connection(half, rs + half, cs + half)
            else:
                node.val = grid[rs][cs]
                node.isLeaf = True

            return node
        return connection(len(grid), 0, 0)