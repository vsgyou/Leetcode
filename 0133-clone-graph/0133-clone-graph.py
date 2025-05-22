"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        # node_dict = {}

        # if not node:
        #     return
        
        # def dfs(node):
            
        #     if node in node_dict:
        #         return node_dict[node]
            
        #     copy_node = Node(node.val)
        #     node_dict[node] = copy_node

        #     for nei in node.neighbors:
        #         copy_node.neighbors.append(dfs(nei))
            
        #     return copy_node
        
        # return dfs(node)

        if not node:
            return 
        
        copy_node = Node(node.val)
        node_dict = {node:copy_node}
        queue = deque([node])

        while queue:
            node = queue.popleft()
            for nei in node.neighbors:
                if nei not in node_dict:
                    node_dict[nei] = Node(nei.val)
                    queue.append(nei)
                node_dict[node].neighbors.append(node_dict[nei])
        
        return copy_node