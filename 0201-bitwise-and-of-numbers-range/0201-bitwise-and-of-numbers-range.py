class Solution(object):
    def rangeBitwiseAnd(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        """
        1 ->    1
        2 ->   10
        3 ->   11

        4 ->  100
        5 ->  101
        6 ->  110
        7 ->  111
        
        8 -> 1000
        9 -> 1001
        10-> 1010
        11-> 1011
        12-> 1100
        13-> 1101
        14-> 1110
        15-> 1111
        """
        shift = 0
        while left <right:
            left >>= 1
            right >>= 1
            shift +=1
        
        return left << shift

        """
        left =  0100 -> 0010 -> 0001 -> 0000 
        right = 1110 -> 0111 -> 0011 -> 0001
        shift =    1 ->    2 ->    3 ->    4

        """