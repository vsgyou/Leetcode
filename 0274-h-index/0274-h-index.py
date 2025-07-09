class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        [6, 5, 3, 1, 0]
        0 -> 5
        1 -> 4
        2 -> 3
        3 -> 2

        """
        citations.sort(reverse = True)
        num_cite = 0
        for i in range(len(citations)):
            if citations[i] >= i+1:
                num_cite += 1
            else:
                break
        return num_cite