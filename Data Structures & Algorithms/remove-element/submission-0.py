class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        write_index = 0

        for v in nums:
            if v != val:
                nums[write_index] = v
                write_index += 1

        return write_index