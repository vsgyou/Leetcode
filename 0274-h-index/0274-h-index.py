class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        num_cite = 0
        citations.sort(reverse = True)
        for index, citation in enumerate(citations):
            if citation >= index + 1:
                num_cite += 1
        
        return num_cite