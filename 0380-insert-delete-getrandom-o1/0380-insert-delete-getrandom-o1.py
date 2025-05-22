import random

class RandomizedSet(object):
    
    def __init__(self):
        """
        Initialize the data structure.
        """
        self.values = []
        self.val_to_idx = {}

    def insert(self, val):
        """
        Inserts an item val into the set if not present.
        :type val: int
        :rtype: bool
        """
        if val in self.val_to_idx:
            return False
        self.values.append(val)
        self.val_to_idx[val] = len(self.values) -1
        return True

    def remove(self, val):
        """
        Removes an item val from the set if present.
        :type val: int
        :rtype: bool
        """
        if val not in self.val_to_idx:
            return False
        last_element = self.values[-1]
        val_idx = self.val_to_idx[val]
        self.values[val_idx] = last_element
        self.val_to_idx[last_element] = val_idx

        self.values.pop()
        del self.val_to_idx[val]
        return True

    def getRandom(self):
        """
        Returns a random element from the set.
        :rtype: int
        """
        return random.choice(self.values)