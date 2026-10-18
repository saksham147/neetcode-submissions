class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        

        stack = []
        def operation(op):
            lastValue = stack[-1]
            secondLastValue = stack[-2]
            stack.pop()
            stack.pop()
            if(op == "+"):
                return secondLastValue + lastValue
            elif(i == "*"):
                return secondLastValue * lastValue
            elif(i == "-"):
                return secondLastValue - lastValue
            elif(i == "/"):
                return int(secondLastValue / lastValue)

        for i in tokens:
            if(i == "+" or i == "*" or i == "-" or i == "/"):
                stack.append(operation(i))
            else:
                stack.append(int(i))


        return stack[0]