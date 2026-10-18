class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        result = {}
        for i in range(len(arr)):

            result[i] = abs(arr[i] - x)

        # Sort items in descending order of value and take top k
        top_k_dict = dict(sorted(result.items(), key=lambda x: x[1])[:k])
        array = []
        for k, v in top_k_dict.items():
            array.append(k)


        array.sort()
        result_arr =[]
        for a in array:
            result_arr.append(arr[a])
    
        return result_arr

