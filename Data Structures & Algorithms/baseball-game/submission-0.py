class Solution:
    def calPoints(self, operations: list[str]) -> int:
        totalArr = []

        for i in range(len(operations)):
            if(operations[i] == "+"):
                totalArr.append(totalArr[-1] + totalArr[-2])
            elif(operations[i] == "D"):
                totalArr.append(totalArr[-1] * 2)
            elif(operations[i] == "C"):
                totalArr.pop(-1)
            else:
                totalArr.append(int(operations[i]))


        return(sum(totalArr))