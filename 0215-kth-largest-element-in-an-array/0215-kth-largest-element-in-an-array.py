from heapq import heappop, heappush

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heap = []
        for num in nums:
            if len(heap) < k:
                heappush(heap, num)
            else:
                if heap[0] < num:
                    heappop(heap)
                    heappush(heap, num)
        return heap[0]