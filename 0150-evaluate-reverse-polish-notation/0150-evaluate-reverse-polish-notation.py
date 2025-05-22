class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for token in tokens:
            if token in {"+","-","*","/"}:
                num2 = stack.pop()
                num1 = stack.pop()

                if token == "+":
                    stack.append(num1 + num2)
                elif token == "-":
                    stack.append(num1 - num2)
                elif token == "*":
                    stack.append(num1 * num2)
                elif token == "/":
                    if num2*num1 < 0:
                        sign = -1
                    else:
                        sign = 1
                    stack.append(sign*(abs(num1) / abs(num2)))
                    
            else:
                stack.append(int(token))
        return stack[0]