class Solution:
    def evalRPN(self, tokens):
        stack = []
        for i in tokens:
            if i == "+":
                stack.append(stack.pop() + stack.pop())

            elif i == "-":
                s, f = stack.pop(), stack.pop()
                res.append(f - s)

            elif i == "*":
                stack.append(stack.pop() * stack.pop())

            elif i == "/":
                s, f = stack.pop(), stack.pop()
                stack.append(int(f / s))

            else:
                stack.append(int(i))
        return stack[0]

tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]

solution = Solution()

print(solution.evalRPN(tokens))
