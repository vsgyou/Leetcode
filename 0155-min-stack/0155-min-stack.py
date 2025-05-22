class MinStack(object):

    def __init__(self):
        self.stack = []
        self.min = []
    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        
        if len(self.min) == 0 or self.min[-1] > val:
            self.min.append(val)
        else:
            self.min.append(self.min[-1])

    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()
        self.min.pop()
        return self.stack
    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min[-1]

