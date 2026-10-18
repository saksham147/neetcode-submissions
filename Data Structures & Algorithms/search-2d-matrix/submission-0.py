class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])
        total = row * col 

        def getPosition(num):
            firstIndex = num // col
            secondIndex = num % col
            return matrix[firstIndex][secondIndex]


        low = 0
        high = total - 1         
        while low <= high:
            mid = (high + low) // 2
            current_val = getPosition(mid)

            if target > current_val:
                low = mid + 1
            elif target < current_val:
                high = mid - 1
            else:
                return True  # Return True if found

        return False  # Return False if not found

