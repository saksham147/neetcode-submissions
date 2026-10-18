class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        array = list(set(nums))
        
        result = 0
        while (result + 1) in array:
            result += 1

        return result + 1