class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        def mergeArr(firstArr, secondArr):
            result = []
            i = 0
            j = 0
            while(i < len(firstArr) and j < len(secondArr)):
                if(firstArr[i] < secondArr[j]):
                    result.append(firstArr[i])
                    i += 1
                else:
                    result.append(secondArr[j])
                    j += 1


            result.extend(firstArr[i:])
            result.extend(secondArr[j:])
            return result



        def mergeSortArr(arr):
            if(len(arr) <= 1):
                return arr

            mid = len(arr) // 2
            leftHalf = arr[:mid]
            rightHalf = arr[mid:]

            sortedLeft = mergeSortArr(leftHalf)
            sortedRight = mergeSortArr(rightHalf)

            return mergeArr(sortedLeft, sortedRight)


        return mergeSortArr(nums)