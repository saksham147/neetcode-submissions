class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        arrange_dict = {}

        for i in nums:
            if i in arrange_dict:
                arrange_dict[i] += 1
            else:
                arrange_dict[i] = 1


        sorted_dict = dict(sorted(arrange_dict.items(), key=lambda item: item[1], reverse=True))

        result = []
        for x in sorted_dict.keys():
            if(k!= 0):
                result.append(x)
                k = k - 1
            else:
                break
        
        return result
