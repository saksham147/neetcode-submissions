class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        subarraysCount = 0
        current_sum = 0
        prefix_counts = {0: 1} 
        for num in nums:
            current_sum += num
            if (current_sum - k) in prefix_counts:
                subarraysCount += prefix_counts[current_sum - k]
            
            prefix_counts[current_sum] = prefix_counts.get(current_sum, 0) + 1

        return subarraysCount
