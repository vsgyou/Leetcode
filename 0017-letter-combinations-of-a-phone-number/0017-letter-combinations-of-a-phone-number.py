class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        digit_dict = {"2":"abc", "3":"def", 
        "4":"ghi", "5":"jkl", "6":"mno", 
        "7":"pqrs", "8":"tuv", "9":"wxyz"}
        
        if not digits:
            return []
        result = []
        
        def backtrack(combination, next_digits):
            if not next_digits:
                return result.append(combination)
            else:
                for letter in digit_dict[next_digits[0]]:
                    backtrack(combination + letter, next_digits[1:])
        
        backtrack("",digits)
        return result