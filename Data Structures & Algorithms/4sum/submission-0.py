class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result = []
        currArr = []
        def kSum(k, start, target):
            if k != 2:
                for i in range(start, len(nums) + 1 - k):
                    if(i>start and nums[i] == nums[i-1]):
                        continue
                    currArr.append(nums[i])
                    kSum(k-1, i+1, target-nums[i])
                    currArr.pop()
                return
            else:
                l = start
                r = len(nums) - 1
                
                while l < r:
                    total = nums[l] + nums[r]
                    if total == target:
                        result.append(currArr + [nums[l], nums[r]])
                        l += 1
                        while l< r and nums[l] == nums[l-1]:
                            l += 1
                    elif total > target:
                        r -= 1
                    elif total < target:
                        l += 1
        kSum(4, 0, target)

        return(result)
