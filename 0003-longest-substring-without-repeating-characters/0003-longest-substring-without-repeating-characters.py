class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_len = 0
        for i in range(len(s)):
            string_set = set()
            for j in range(i, len(s)):
                string_set.add(s[j])
                if len(string_set) == j-i+1:
                   max_len = max(max_len, j-i+1)
                else:
                    break

        return max_len
        
        # 시간 오래걸림 -> Sliding Window
        # start, end = 0, 0
        # max_len = 0
        # s_set = set()
        # while end < len(s):
        #     if s[end] not in s_set:
        #         s_set.add(s[end])
        #         max_len = max(max_len, end-start+1)
        #         end += 1
        #     else:
        #         s_set.remove(s[start])
        #         start +=1

        # return max_len