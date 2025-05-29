from collections import deque

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # 너비 우선 탐색
        queue = deque([(0,0)])
        visited = set()
        while queue:
            count, total = queue.popleft()
            if total == amount:
                return count
            if total in visited:
                continue
            visited.add(total)
            for coin in coins:
                if total < amount:
                    queue.append((count + 1, total + coin))
        return -1
    """
    queue = [(동전 수, 가진 최종 금액)]
    너비 우선 탐색으로, 최소의 동전 수로 금액을 맞출 수 있는 경우를 찾는다.
    """
    # DP 방법
