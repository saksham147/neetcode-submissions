# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:
class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        length = mountainArr.length()
        

        def getMountainPeak():
            low = 0
            high = length - 1
            while low < high:
                mid = (low + high) // 2
                if mountainArr.get(mid) < mountainArr.get(mid + 1):
                    low = mid + 1
                else:
                    high = mid
            return low

        peak = getMountainPeak()

        # 2. Left Search (Ascending order)
        l, r = 0, peak
        while l <= r:
            m = (l + r) // 2
            value = mountainArr.get(m)

            if value > target:
                r = m - 1
            elif value < target:
                l = m + 1
            else:
                return m

        # 3. Right Search (Descending order)
        l, r = peak, length - 1
        while l <= r:
            m = (l + r) // 2
            value = mountainArr.get(m)
            
            if value < target:
                r = m - 1 
            elif value > target:
                l = m + 1 
            else:
                return m

        return -1