from collections import deque

class Solution(object):
    def minMutation(self, startGene, endGene, bank):
        """
        :type startGene: str
        :type endGene: str
        :type bank: List[str]
        :rtype: int
        """
    
        if endGene not in bank:
            return -1

        queue = deque([(startGene, 0)])
        genes = ["A","C","G","T"]
        while queue:
            current_gene, moves = queue.popleft()
            if current_gene == endGene:
                return moves
                
            for i in range(len(current_gene)):
                for gene in genes:
                    test_gene = current_gene[:i] + gene + current_gene[i+1:]
                    if test_gene in bank:
                        queue.append((test_gene, moves+1))
                        bank.remove(test_gene)
        return -1