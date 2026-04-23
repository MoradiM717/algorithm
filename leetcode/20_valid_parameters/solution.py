class Solution:
    ACCEPTABLE = {"(", "{", "["}
    MAPPER = {
        "(": ")",
        "{": "}",
        "[": "]"
    }

    def pick_top(self, stack):
        if stack:
            return stack[-1]
        return None

    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char in self.ACCEPTABLE:
                stack.append(char)

            else:
                if stack and char != self.MAPPER[self.pick_top(stack)]:
                    return False
                if stack: stack.pop()
                else: return False

        return not stack

s = Solution()
print(s.isValid("]"))