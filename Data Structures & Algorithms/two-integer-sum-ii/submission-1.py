class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        point_first = 0
        point_Second = len(numbers) - 1

        while True:
            total = numbers[point_first] + numbers[point_Second]

            if total == target:
                return [point_first + 1, point_Second + 1]
                break
            elif total > target:
                point_Second = point_Second - 1
            elif total < target:
                point_first = point_first + 1