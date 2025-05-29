class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # digits[-1] = digits[-1]+1
        # digits = [0] + digits
        # next_num = 0 
        # result = []
        # while digits:
        #     digit = digits.pop()
        #     digit = next_num + digit
        #     next_num = digit // 10
        #     current_num = digit % 10

        #     result.append(current_num)
        # result = result[::-1]
        # if result[0] == 0:
        #     result = result[1:]
        # return result
        
        num = int("".join(map(str, digits))) + 1
        return list(map(int, str(num)))