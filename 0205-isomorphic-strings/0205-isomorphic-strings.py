class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_dict = dict()
        for i in range(len(s)):
            if s[i] not in s_dict:
                s_dict[s[i]] = t[i]
            else:
                if s_dict[s[i]] != t[i]:
                    return False
        t_dict = dict()
        for i in range(len(t)):
            if t[i] not in t_dict:
                t_dict[t[i]] = s[i]
            else:
                if t_dict[t[i]] != s[i]:
                    return False
        return True