class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        
        Example) n = 2

        (
            (
                ( ❌
                )
                    ( ❌
                    ) ✅ "(())"   
            )
                (
                    ( ❌
                    ) ✅ "()()"
                ) ❌
        ) ❌

        """
        result = []

        def dfs(text, opening, closing):
            # 기저조건 1: "("개수와 ")"개수가 n과 같을때, 조건을 만족시킴
            if opening == n and closing == n:
                return result.append(text)
            # 기저조건 2: "(" 개수가 n보다 크거나, ")" 개수보다 큰 경우, 조건 불만족
            if opening > n or opening < closing:
                return
            
            dfs(text + "(", opening+1, closing)
            dfs(text + ")", opening, closing+1)
        
        dfs("",0,0)
        return result

