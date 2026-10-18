class Solution:
    def mySqrt(self, x: int) -> int:
        low = 0
        high = x
        result = 0
        while low <= high:
            mid = low + (high - low) // 2

            if mid * mid < x:
                low = mid + 1
                result = mid
            elif mid * mid > x:
                high = mid - 1
            else:
                return mid

        return result
        
        