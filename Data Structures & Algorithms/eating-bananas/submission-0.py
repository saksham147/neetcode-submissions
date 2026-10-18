import math

class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        low = 1
        high = max(piles)

        while low < high:
            mid = (low + high) // 2
            hr = 0

            for i in piles:
                hr += math.ceil(i / mid)

            if hr <= h:
                high = mid
            else:
                low = mid + 1
        return high