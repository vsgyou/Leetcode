class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        unique_dict = {}

        for word in strs:
            sorted_word = ''.join(sorted(word))
            
            if sorted_word not in unique_dict:
                unique_dict[sorted_word] = []
            unique_dict[sorted_word].append(word)
        return unique_dict.values()