class Solution:
    def isValid(self, s):
        stack = []

        matching = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        for bracket in s:
            if bracket in matching:
                if stack:
                    last_open = stack[-1]
                else:
                    last_open = None

                if last_open == matching[bracket]:
                    stack.pop()
                else:
                    return False

            else:
                stack.append(bracket)
        return len(stack) == 0
