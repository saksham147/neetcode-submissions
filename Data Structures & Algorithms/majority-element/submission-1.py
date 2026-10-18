class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        s = dict()

        for i in nums:
            if(i in s):
                s[i] =  s[i] + 1
            else:
                s[i] =  1

        maxValue = 0
        val = 0
        for x in s:
            if(maxValue < s[x]):
                maxValue = s[x]
                val = x

        return(val)