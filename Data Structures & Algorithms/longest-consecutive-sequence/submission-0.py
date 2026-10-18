class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longestSeq = 0

        for n in nums:
            if (n-1) not in numSet:
                length = n + 1
                while (length) in numSet:
                    length += 1

                longestSeq = max(length - n, longestSeq)
        return longestSeq