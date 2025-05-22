class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or len(s) <= numRows:
            return s

        result = [""] * numRows
        up_or_down = False
        count = 0

        for i in range(len(s)):
            result[count] += s[i]
            if count == 0 or count == numRows-1:
                up_or_down = not up_or_down

            if up_or_down:
                count += 1
            else:
                count -= 1
        return "".join(result)