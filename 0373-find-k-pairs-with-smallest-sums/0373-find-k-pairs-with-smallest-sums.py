from heapq import heappush, heappop

class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        result = []
        min_heap = []
        
        # nums1의 처음 k개 요소와 nums2의 첫 번째 요소를 힙에 넣음
        for i in range(min(k, len(nums1))):
            heappush(min_heap, (nums1[i] + nums2[0], i, 0))
        
        while k > 0 and min_heap:
            sum_val, i, j = heappop(min_heap)
            result.append([nums1[i], nums2[j]])
            k -= 1  # k개만 유지
            
            # nums2에서 다음 요소가 있다면 추가 (불필요한 요소 추가 방지)
            if j + 1 < len(nums2):
                heappush(min_heap, (nums1[i] + nums2[j + 1], i, j + 1))

        return result