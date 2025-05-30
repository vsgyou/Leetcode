class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # def is_Palindrome(start,end):
        #     while start < end:
        #         if s[start] != s[end]:
        #             return False
        #         start +=1 
        #         end -= 1
        #     return True
        # max_s, max_e = 0, 0
        # for i in range(len(s)):
        #     for j in range(i+1,len(s)):
        #         if is_Palindrome(i, j) and (max_e - max_s) < (j - i):
        #             max_s, max_e = i, j
        # return s[max_s:max_e+1]
        
        # 시간복잡도 개선
        max_start, max_end = 0, 0
        for i in range(len(s)):
            start, end = i, i
            while 0 <= start and end < len(s) and s[start] == s[end]:
                if (max_end - max_start) < (end - start):
                    max_start, max_end = start, end
                start, end = start - 1, end + 1
            start, end = i, i+1
            while 0 <= start and end < len(s) and s[start] == s[end]:
                if (max_end - max_start) < (end - start):
                    max_start, max_end = start, end
                start, end = start - 1, end + 1
            
        return s[max_start:max_end+1]