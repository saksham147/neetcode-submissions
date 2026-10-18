class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        

        stack = []

        for i in tokens:
            if(i == "+"):
                lastValue = stack[-1]
                secondLastValue = stack[-2]
                stack.pop()
                stack.pop()
                stack.append(secondLastValue + lastValue)

            elif(i == "*"):
                lastValue = stack[-1]
                secondLastValue = stack[-2]
                stack.pop()
                stack.pop()
                stack.append(secondLastValue * lastValue)
            elif(i == "-"):
                lastValue = stack[-1]
                secondLastValue = stack[-2]
                stack.pop()
                stack.pop()
                stack.append(secondLastValue - lastValue)
            elif(i == "/"):
                lastValue = stack[-1]
                secondLastValue = stack[-2]
                stack.pop()
                stack.pop()
                stack.append(int(secondLastValue / lastValue))
            else:
                stack.append(int(i))


        return(stack[0])