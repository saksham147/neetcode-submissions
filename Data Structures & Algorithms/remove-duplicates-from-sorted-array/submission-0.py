class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        writeindex = 1
        for i in range(1, len(nums)):
            if(nums[i] != nums[i-1]):
                nums[writeindex] = nums[i]
                writeindex = writeindex + 1

        return writeindex