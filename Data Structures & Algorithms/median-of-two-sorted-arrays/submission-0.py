class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        final_arr = nums1 + nums2
        final_arr.sort()

        if(len(final_arr) % 2 == 0):
            a = (len(final_arr) // 2) - 1
            b = a + 1 
            result = (final_arr[a] + final_arr[b])/2
        else:
            a = len(final_arr) // 2
            result = float(final_arr[a])

        return result