class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort(reverse = True)
        num_cite = 0
        for i, citation in enumerate(citations):
            if citation >= i+1:
                num_cite += 1
        return num_cite