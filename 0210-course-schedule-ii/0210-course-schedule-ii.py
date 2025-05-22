class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        graph = {i: [] for i in range(numCourses)}
        for curr, pre in prerequisites:
            graph[curr].append(pre)
        
        traversing = set()
        finished = set()
        ordered = []

        def dfs(curr):
            if curr in traversing:
                return False
            if curr in finished:
                return True
            
            traversing.add(curr)
            for pre in graph[curr]:
                if not dfs(pre):
                    return False
            traversing.remove(curr)
            finished.add(curr)
            ordered.append(curr)
            return True

        for c in range(numCourses):
            if not dfs(c):
                return []
        return ordered
        