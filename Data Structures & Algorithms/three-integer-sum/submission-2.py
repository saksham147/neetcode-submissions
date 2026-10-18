class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i, a in enumerate(nums):
            if(i > 0 and a == nums[i-1]):
                continue

            target = 0
            l = i + 1
            r = len(nums) - 1

            while l < r:
                total = nums[l] + nums[r] + a
                if total == target:
                    result.append([a,nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
                elif total > target:
                    r -= 1
                elif total < target:
                    l += 1


        return result
