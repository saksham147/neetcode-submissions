class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        lengh = len(s)

        if(lengh % 2 == 0):
            ran = lengh // 2
        else:
            ran = (lengh // 2) + 1
        for i in range(ran):
            lastVal = s[lengh-i-1]
            firstVal = s[i]

            s[i] = lastVal
            s[lengh-i-1] = firstVal