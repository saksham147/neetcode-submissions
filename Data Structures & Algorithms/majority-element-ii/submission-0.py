class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        n = len(nums)
        dictMap = {}

        for i in nums:
            if i in dictMap:
                dictMap[i] += 1
            else:
                dictMap[i] = 1
        result = []
        for key, value in dictMap.items():
            if (n // 3) < value:
                result.append(key)

        return result
