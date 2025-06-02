import random

class RandomizedSet(object):
    
    def __init__(self):
        """
        Initialize the data structure.
        """
        self.nums= []



    def insert(self, val):
        """
        Inserts an item val into the set if not present.
        :type val: int
        :rtype: bool
        """
        if val not in self.nums:
            self.nums.append(val)
            return True
        else:
            return False

    def remove(self, val):
        """
        Removes an item val from the set if present.
        :type val: int
        :rtype: bool
        """
        if val in self.nums:
            self.nums.remove(val)
            return True
        else:
            return False

    def getRandom(self):
        """
        Returns a random element from the set.
        :rtype: int
        """
        return random.choice(self.nums)