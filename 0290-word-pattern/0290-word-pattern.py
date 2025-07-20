class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        words = s.split()
        
        if len(pattern) != len(words):
            return False

        p2w = {}
        w2p = {}

        for i in range(len(pattern)):
            if pattern[i] in p2w:
                if p2w[pattern[i]] != words[i]:
                    return False
            else:
                p2w[pattern[i]] = words[i]
            
            if words[i] in w2p:
                if w2p[words[i]] != pattern[i]:
                    return False
            else:
                w2p[words[i]] = pattern[i]
        return True