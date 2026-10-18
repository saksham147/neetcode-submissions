import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub('[^A-Za-z0-9]+', '', s).replace(" ", "").lower()

        lengh = len(s)

        if(lengh % 2 == 0):
            ran = lengh // 2
        else:
            ran = (lengh // 2) + 1
        for i in range(ran):
            lastVal = s[lengh-i-1]
            firstVal = s[i]

            if(lastVal != firstVal):
                return(False)

        return True
