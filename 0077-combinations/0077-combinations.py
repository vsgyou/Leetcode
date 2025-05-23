class Solution:
    def combine(self, n, k):
        result = []
        def backtrack(elements, start, k):
            if k == 0:
                result.append(elements[:])
            for i in range(start, n+1):
                elements.append(i)
                backtrack(elements, i+1, k-1)
                elements.pop()
        backtrack([],1,k)


            
        return result