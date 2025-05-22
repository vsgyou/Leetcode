class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = {i:[] for i in range(numCourses)}
        for curr, pre in prerequisites:
            graph[curr].append(pre)
        
        traversing = set()
        finished = set()

        def can_finish(curr):
            if curr in traversing:
                return False
            if curr in finished:
                return True
            
            traversing.add(curr)
            for pre in graph[curr]:
                if not can_finish(pre):
                    return False
            
            traversing.remove(curr)
            finished.add(curr)
            return True

        for curr in graph:
            if not can_finish(curr):
                return False
        return True
                