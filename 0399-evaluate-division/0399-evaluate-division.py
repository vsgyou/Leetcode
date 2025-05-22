from collections import defaultdict

class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        graph = defaultdict(dict)
        for (A,B),value in zip(equations, values):
            graph[A][B] = value
            graph[B][A] = 1/value
        
        def dfs(first, second, visited):
            if first not in graph or second not in graph:
                return -1.0
            if second in graph[first]:
                return graph[first][second]
            
            visited.add(first)

            for neighbor in graph[first]:
                if not neighbor in visited:
                    temp_result = dfs(neighbor, second, visited)
                    if temp_result != -1.0:
                        return graph[first][neighbor]*temp_result
            return -1.0
        
        results = []
        for C,D in queries:
            results.append(dfs(C,D,set()))

        return results
        